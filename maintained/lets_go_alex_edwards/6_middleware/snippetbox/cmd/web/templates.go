package main

import (
	"html/template"
	"net/http"
	"path/filepath"
	"time"

	"snippetbox.letsgo.foxcodenine/internal/models"
)

// ---------------------------------------------------------------------

// templateData holds the dynamic data passed into HTML templates.
type templateData struct {
	CurrentYear int
	Snippet     *models.Snippet
	Snippets    []*models.Snippet
}

// ---------------------------------------------------------------------

// Create an newTemplateData() helper, which returns a pointer to a templateData
// struct initialized with the current year.
func (app *application) newTemplateData(r *http.Request) *templateData {
	return &templateData{
		CurrentYear: time.Now().Year(),
	}
}

// ---------------------------------------------------------------------
// Custom template functions

// humanDate formats a time.Time into a human-readable string.
func humanDate(t time.Time) string {
	return t.Format("02 Jan 2006 at 15:04")
}

// global variable "functions" maps template function names to their implementations.
// This lets templates call our custom helpers (e.g. {{humanDate .Created}}).
var functions = template.FuncMap{
	"humanDate": humanDate,
}

// ---------------------------------------------------------------------

func newTemplateCache() (map[string]*template.Template, error) {

	tc := map[string]*template.Template{}

	// Find all page templates matching "./ui/html/pages/*.tmpl".
	// Returns a slice of file paths like [home.tmpl, view.tmpl].
	pages, err := filepath.Glob("./ui/html/pages/*.tmpl.html")
	if err != nil {
		return nil, err
	}

	for _, page := range pages {

		// Extract the file name (like 'home.tmpl') from the full filepath
		name := filepath.Base(page)

		// -----------------------------------------------
		// Parse the base template file into a template set.
		// ts, err := template.ParseFiles("./ui/html/base.tmpl.html")
		// if err != nil {
		// 	return nil, err
		// }
		// -----------------------------------------------

		// To use custom helpers (from functions), we must register FuncMap *before* parsing templates. So we:
		// 1) Create a new template set with template.New(name)
		// 2) Attach FuncMap with Funcs(functions)
		// 3) Parse the template file(s) as usual.
		ts, err := template.New(name).Funcs(functions).ParseFiles("./ui/html/base.tmpl.html")
		if err != nil {
			return nil, err
		}

		// Call ParseGlob() *on this template set* to add any partials.
		ts, err = ts.ParseGlob("./ui/html/partials/*.tmpl.html")
		if err != nil {

			return nil, err
		}

		// Call ParseFiles() *on this template set* to add the page template.
		ts, err = ts.ParseFiles(page)
		if err != nil {

			return nil, err
		}

		// Add the template set to the map, using the name of the page
		tc[name] = ts

	}

	return tc, nil
}

// -------------------------------

func newTemplateCache_oldVersion() (map[string]*template.Template, error) {

	tc := map[string]*template.Template{}

	// Find all page templates matching "./ui/html/pages/*.tmpl".
	// Returns a slice of file paths like [home.tmpl, view.tmpl].
	pages, err := filepath.Glob("./ui/html/pages/*.tmpl.html")
	if err != nil {
		return nil, err
	}

	for _, page := range pages {

		// Extract the file name (like 'home.tmpl') from the full filepath
		name := filepath.Base(page)

		// Create a slice containing the filepaths for our base template, any
		// partials and the page.
		files := []string{
			"./ui/html/base.tmpl.html",
			"./ui/html/partials/nav.tmpl.html",
			page,
		}

		// Parse the files into a template set.
		ts, err := template.ParseFiles(files...)
		if err != nil {
			return nil, err
		}

		// Add the template set to the map, using the name of the page
		tc[name] = ts

	}

	return tc, nil
}

// ---------------------------------------------------------------------
