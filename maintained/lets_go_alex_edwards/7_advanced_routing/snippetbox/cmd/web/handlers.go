package main

import (
	"errors"
	"fmt"
	"net/http"
	"path/filepath"
	"strconv"

	"github.com/julienschmidt/httprouter"
	"snippetbox.letsgo.foxcodenine/internal/models"
)

// ---------------------------------------------------------------------

func (app *application) home(w http.ResponseWriter, r *http.Request) {

	if r.URL.Path != "/" {
		app.NotFound(w)
		return
	}

	// panic("oops! something went wrong") // Deliberate panic

	// Get the latest 10 snippets from the DB.
	snippets, err := app.Snippets.Latest()
	if err != nil {
		app.ServerError(w, err)
		return
	}

	// --------------------------------------

	// for _, snippet := range snippets {
	// 	fmt.Fprintf(w, "%+v\n", snippet)
	// }

	// return
	// --------------------------------------

	// Create an instance of a templateData struct holding the snippet data.
	// Usinf app.newTemplateDate to  containing the 'default' data
	td := app.newTemplateData(r)
	td.Snippets = snippets

	app.render(w, 200, "home.tmpl.html", td)
}

// ---------------------------------------------------------------------

func (app *application) snippetView(w http.ResponseWriter, r *http.Request) {

	parmas := httprouter.ParamsFromContext(r.Context())

	id, err := strconv.Atoi(parmas.ByName("id"))

	if err != nil || id < 1 {
		// http.NotFound(w, r)
		app.NotFound(w)
		return
	}

	// --------------------------------------
	// w.Write([]byte("Display a specific snippet..."))
	// fmt.Fprintf(w, "Display a specific snippet with ID %d...", id)
	// --------------------------------------

	snippet, err := app.Snippets.Get(id)
	if err != nil {
		if errors.Is(err, models.ErrNoRecord) {
			app.NotFound(w)
		} else {
			app.ServerError(w, err)
		}
		return
	}

	// --------------------------------------
	// fmt.Fprintf(w, "%v", snippet)
	// --------------------------------------

	// Create an instance of a templateData struct holding the snippet data.
	// Usinf app.newTemplateDate to  containing the 'default' data
	td := app.newTemplateData(r)
	td.Snippet = snippet

	// Pass the data to the render() helper
	app.render(w, 200, "view.tmpl.html", td)
}

// ---------------------------------------------------------------------

func (app *application) snippetCreate(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("Display the form for creating new snippet..."))
}

func (app *application) snippetCreatePost(w http.ResponseWriter, r *http.Request) {

	if r.Method != "POST" {

		// --------------------------------------
		// w.WriteHeader(405)
		// w.Write([]byte("Method Not Allowed"))
		// --------------------------------------

		w.Header().Set("Allow", http.MethodPost)
		app.ClientError(w, http.StatusMethodNotAllowed)

		// --------------------------------------
		// http.Error(w, "Method Not Allowed", http.StatusMethodNotAllowed)
		// --------------------------------------
		return
	}

	title := "O snail"
	content := "O snail\nClimb Mount Fuji,\nBut slowly, slowly!\n\n– Kobayashi Issa"
	expires := 7

	id, err := app.Snippets.Insert(title, content, expires)
	if err != nil {
		app.ServerError(w, err)
		return
	}

	// --------------------------------------
	// w.Write([]byte("Create a new snippet..."))
	// --------------------------------------

	http.Redirect(w, r, fmt.Sprintf("/snippet/view?id=%d", id), http.StatusSeeOther)
}

// ---------------------------------------------------------------------

func (app *application) jsonSnippet(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	w.Write([]byte(`{"name": "dorothy"}`))
}

// downloadHandler -----------------------------------------------------

func (app *application) downloadHandler(w http.ResponseWriter, r *http.Request) {
	file := r.URL.Query().Get("file")
	if file == "" {

		// --------------------------------------
		// http.Error(w, "missing file parameter", http.StatusBadRequest)
		// --------------------------------------

		app.ClientError(w, http.StatusBadRequest)
	}

	// Clean the path to avoid directory traversal (e.g. "../etc/passwd")
	cleanPath := filepath.Clean("./ui/static/" + file)

	http.ServeFile(w, r, cleanPath)
}
