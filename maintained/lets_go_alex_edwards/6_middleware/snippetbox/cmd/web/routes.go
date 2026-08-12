package main

import (
	"net/http"

	"github.com/justinas/alice"
)

// Change routes() to return http.Handler (the interface) instead of *http.ServeMux.
// This gives flexibility: middlewares like secureHeaders wrap any http.Handler,
// not just *http.ServeMux.
func (app *application) Routes() http.Handler {

	mux := http.NewServeMux()

	// Create a file server which serves files out of the "./ui/static" directory.
	fileServer := http.FileServer(http.Dir("./ui/static/"))

	// Use the mux.Handle() function to register the file server as the handler for
	// all URL paths that start with "/static/". For matching paths, we strip the
	// "/static" prefix before the request reaches the file server.

	mux.Handle("/static/", http.StripPrefix("/static", fileServer))

	mux.HandleFunc("/", app.home)
	mux.HandleFunc("/snippet/view", app.snippetView)
	mux.HandleFunc("/snippet/create", app.snippetCreate)

	// Same as mux.HandleFunc but shows explicitly that a function is being converted into an http.Handler
	mux.Handle("/snippet/json", http.HandlerFunc(app.jsonSnippet))

	// Example download handler with ServeFile + filepath.Clean
	mux.HandleFunc("/download", app.downloadHandler)

	// return app.RecoverPanic(app.LogRequest(secureHeaders(mux)))

	standard := alice.New(app.RecoverPanic, app.LogRequest, secureHeaders)

	return standard.Then(mux)
}
