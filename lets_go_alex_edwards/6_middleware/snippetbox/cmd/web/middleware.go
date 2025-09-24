package main

import (
	"fmt"
	"net/http"
)

// Security headers:
// Content-Security-Policy → restricts sources for scripts, styles, fonts, etc. (mitigates XSS).
// Referrer-Policy → controls how much referrer info is shared with other sites.
// X-Content-Type-Options → prevents browsers from guessing MIME types (stops "sniffing").
// X-Frame-Options → blocks the site from being embedded in iframes (clickjacking protection).
// X-XSS-Protection → disables old browser XSS filters (modern CSP is safer).

func secureHeaders(next http.Handler) http.Handler {

	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {

		w.Header().Set("Content-Security-Policy", "default-src 'self'; style-src 'self' fonts.googleapis.com; font-src fonts.gstatic.com")
		w.Header().Set("Referrer-Policy", "origin-when-cross-origin")
		w.Header().Set("X-Content-Type-Options", "nosniff")
		w.Header().Set("X-Frame-Options", "deny")
		w.Header().Set("X-XSS-Protection", "0")

		next.ServeHTTP(w, r)
	})
}

// ---------------------------------------------------------------------

func (app *application) LogRequest(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		app.InfoLog.Printf("%s - %s %s %s", r.RemoteAddr, r.Proto, r.Method, r.URL.RequestURI())
		next.ServeHTTP(w, r)
	})
}

// ---------------------------------------------------------------------

// recoverPanic wraps a handler and converts panics into a 500 response (no process crash).
func (app *application) RecoverPanic(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {

		// Defer a recovery func so it runs after the handler (even if it panics).
		defer func() {

			// If a panic occurred, recover it.
			if err := recover(); err != nil {

				// Ask the client not to reuse this connection (safer after a panic).
				w.Header().Set("Connection", "close")

				// Log + send a 500 Internal Server Error.
				app.ServerError(w, fmt.Errorf("%s", err))
			}
		}()

		// Call the next handler in the chain.
		next.ServeHTTP(w, r)
	})
}

// ---------------------------------------------------------------------
