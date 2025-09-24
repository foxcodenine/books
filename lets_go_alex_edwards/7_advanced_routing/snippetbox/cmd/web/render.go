package main

import (
	"bytes"
	"fmt"
	"net/http"
)

func (app *application) render(w http.ResponseWriter, status int, page string, td *templateData) {
	// Look up the template set in the cache (e.g. "home.tmpl").
	ts, ok := app.TemplateCache[page]
	if !ok {
		err := fmt.Errorf("the template %s does not exist", page)
		app.ServerError(w, err)
		return
	}

	// Write the template to the buffer, instead of straight to the
	// http.ResponseWriter, to avoid partial writes on error.
	// "base" is the root layout (HTML skeleton) that pulls in nav + page content.
	// We always start rendering from here so the full page is built correctly
	buf := new(bytes.Buffer)
	err := ts.ExecuteTemplate(buf, "base", td) // always start from "base" layout
	if err != nil {
		app.ServerError(w, err)
		return
	}

	// Safe to write status code now (only after template executed successfully).
	w.WriteHeader(status)

	// Copy the rendered template from buffer to response.
	buf.WriteTo(w)
}
