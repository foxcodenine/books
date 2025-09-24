package main

import (
	"net/http"

	"github.com/julienschmidt/httprouter"
	"github.com/justinas/alice"
)

// Change routes() to return http.Handler (the interface) instead of *http.ServeMux.
// This gives flexibility: middlewares like secureHeaders wrap any http.Handler,
// not just *http.ServeMux.
func (app *application) Routes() http.Handler {

	// Initialize a new httprouter instance.
	router := httprouter.New()

	// Use a custom 404 handler by wrapping app.notFound.
	// You can also set router.MethodNotAllowed the same way.
	router.NotFound = http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		app.NotFound(w)
	})

	// Serve static files from ./ui/static at /static/*.
	// The *filepath param lets httprouter pass the remainder of the URL to the file server.
	fileServer := http.FileServer((http.Dir("./ui/static/")))
	router.Handler(http.MethodGet, "/static/*filepath", http.StripPrefix("/static", fileServer))

	// Register application routes.
	// httprouter provides :param syntax (e.g. :id) for path parameters.
	router.HandlerFunc(http.MethodGet, "/", app.home)
	router.HandlerFunc(http.MethodGet, "/snippet/view/:id", app.snippetView)
	router.HandlerFunc(http.MethodGet, "/snippet/create", app.snippetCreate)
	router.HandlerFunc(http.MethodPost, "/snippet/create", app.snippetCreatePost)

	// Same as mux.HandleFunc but shows explicitly that a function is being converted into an http.Handler
	router.HandlerFunc(http.MethodGet, "/snippet/json", app.jsonSnippet)

	router.HandlerFunc(http.MethodGet, "/download", app.downloadHandler)

	//  Create the middleware chain as normal.
	standard := alice.New(app.RecoverPanic, app.LogRequest, secureHeaders)

	//  Wrap the router with the middleware and return it as normal.
	return standard.Then(router)

}
