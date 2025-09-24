package main

import (
	"log"
	"net/http"
)

// main ----------------------------------------------------------------

func main() {

	// routers --------------------------------------

	mux := http.NewServeMux()

	// Create a file server which serves files out of the "./ui/static" directory.

	fileServer := http.FileServer(http.Dir("./ui/static/"))

	// Use the mux.Handle() function to register the file server as the handler for
	// all URL paths that start with "/static/". For matching paths, we strip the
	// "/static" prefix before the request reaches the file server.

	mux.Handle("/static/", http.StripPrefix("/static", fileServer))

	mux.HandleFunc("/", home)
	mux.HandleFunc("/snippet/view", snippetView)
	mux.HandleFunc("/snippet/create", snippetCreate)

	// Same as mux.HandleFunc but shows explicitly that a function is being converted into an http.Handler
	mux.Handle("/snippet/json", http.HandlerFunc(jsonSnippet))

	// Example download handler with ServeFile + filepath.Clean
	mux.HandleFunc("/download", downloadHandler)

	// run http server ------------------------------

	log.Println("Starting server on :4000")
	err := http.ListenAndServe(":4000", mux)

	if err != nil {
		log.Fatal(err)
	}
}
