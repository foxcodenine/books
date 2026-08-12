package main

import (
	"errors"
	"fmt"
	"net/http"
	"path/filepath"
	"strconv"
	"text/template"

	"snippetbox.letsgo.foxcodenine/internal/models"
)

// ---------------------------------------------------------------------

func (app *application) home(w http.ResponseWriter, r *http.Request) {

	if r.URL.Path != "/" {
		app.NotFound(w)
		return
	}

	// -----------------------------------------------------------------

	snippets, err := app.Snippets.Latest()
	if err != nil {
		app.ServerError(w, err)
		return
	}

	for _, snippet := range snippets {
		fmt.Fprintf(w, "%+v\n", snippet)
	}

	// -----------------------------------------------------------------
	return

	// Create a slice with file paths. The base template must come first.
	files := []string{
		"./ui/html/base.tmpl.html",
		"./ui/html/partials/nav.tmpl.html",
		"./ui/html/pages/home.tmpl.html",
	}

	// Use the template.ParseFiles() function to read the template file into a template set.
	// On error, log details and return a generic 500 response to the user.
	ts, err := template.ParseFiles(files...)
	if err != nil {
		app.ServerError(w, err)
		return
	}

	// Use the ExecuteTemplate() method to write the content of the "base"
	// template as the response body.
	// We pass nil for now as there's no dynamic data.
	err = ts.ExecuteTemplate(w, "base", nil)
	if err != nil {
		app.ServerError(w, err)
	}

	// w.Write([]byte("Hello from Sinppetbox"))

}

// ---------------------------------------------------------------------

func (app *application) snippetView(w http.ResponseWriter, r *http.Request) {
	id, err := strconv.Atoi(r.URL.Query().Get("id"))

	if err != nil || id < 1 {
		// http.NotFound(w, r)
		app.NotFound(w)
		return
	}

	// w.Write([]byte("Display a specific snippet..."))
	// fmt.Fprintf(w, "Display a specific snippet with ID %d...", id)

	snippet, err := app.Snippets.Get(id)
	if err != nil {
		if errors.Is(err, models.ErrNoRecord) {
			app.NotFound(w)
		} else {
			app.ServerError(w, err)
		}
		return
	}

	fmt.Fprintf(w, "%v", snippet)
}

// ---------------------------------------------------------------------

func (app *application) snippetCreate(w http.ResponseWriter, r *http.Request) {

	if r.Method != "POST" {

		// w.WriteHeader(405)
		// w.Write([]byte("Method Not Allowed"))

		w.Header().Set("Allow", http.MethodPost)
		// http.Error(w, "Method Not Allowed", http.StatusMethodNotAllowed)
		app.ClientError(w, http.StatusMethodNotAllowed)

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

	// w.Write([]byte("Create a new snippet..."))
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
		// http.Error(w, "missing file parameter", http.StatusBadRequest)
		app.ClientError(w, http.StatusBadRequest)
	}

	// Clean the path to avoid directory traversal (e.g. "../etc/passwd")
	cleanPath := filepath.Clean("./ui/static/" + file)

	http.ServeFile(w, r, cleanPath)
}
