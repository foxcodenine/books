package main

import (
	"flag"
	"log"
	"net/http"
	"os"
)

// Application - hold the application-wide dependencies for the web application.
type application struct {
	ErrorLog *log.Logger
	InfoLog  *log.Logger
}

// main ------------------------------------------------------------------------

func main() {

	// flages -----------------------------------------------------------

	// Define a new command-line flag with the name 'addr', a default value of ":4000"
	// and some short help text explaining what the flag controls.

	addr := flag.String("addr", ":4000", "HTTP network address")

	// Importantly, we use the flag.Parse() function to parse the command-line flag.
	// Otherwise it will always contain the default value of ":4000"

	flag.Parse()

	// logger ----------------------------------------------------------

	infoLog := log.New(os.Stdout, "INFO\t", log.Ldate|log.Ltime)
	errorLog := log.New(os.Stderr, "ERROR\t", log.Ldate|log.Ltime|log.Lshortfile)

	// app -------------------------------------------------------------
	// Initialize a new instance of our application struct

	app := &application{
		ErrorLog: errorLog,
		InfoLog:  infoLog,
	}

	// run http server -------------------------------------------------

	infoLog.Printf("Starting server on %s", *addr)

	// Start the HTTP server using the custom server configuration (address, error logger, and handler).
	srv := &http.Server{
		Addr:     *addr,
		ErrorLog: errorLog,
		Handler:  app.Routes(),
	}
	err := srv.ListenAndServe()

	if err != nil {
		errorLog.Fatal(err)
	}
}
