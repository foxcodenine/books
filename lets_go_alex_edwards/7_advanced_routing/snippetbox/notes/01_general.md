https://www.youtube.com/watch?v=8hOXXkcsR5Q

<!-- --------------------------------------------------------------- -->

<!-- initialize a new Go module and create go.mod -->
go mod init snippetbox.letsgo.foxcodenine

<!-- run the main package in the current directory -->
go run .

<!--  passing command-line flag  -->
go run ./cmd/web -addr=":9999"

<!-- list all the available command-line flags -->
go run ./cmd/web -help


<!--  passing the environment variable as a command-line flag  -->
export SNIPPETBOX_ADDR=":9999"
go run ./cmd/web -addr=$SNIPPETBOX_ADDR

<!-- redirect the stdout and stderr streams to on-disk files -->
go run ./cmd/web >>/tmp/info.log 2>>/tmp/error.log

<!-- download all dependencies listed in go.mod into the local module cache -->
go mod download


<!-- upgrade to latest available usinf flag -u -->
go get -u github.com/foo/bar

<!-- upgrade to a specific version -->
go get -u github.com/foo/bar@v2.0.0

<!-- removing unused packages -->
go get github.com/foo/bar@none

<!-- remove any unused packages -->
go mod tidy -v

<!-- --------------------------------------------------------------- -->

Go best practices, six years in
https://peter.bourgon.org/go-best-practices-2016/#development-environment

Golang Interfaces explained
https://www.alexedwards.net/blog/interfaces-explained

Understanding Mutexes
https://www.alexedwards.net/blog/understanding-mutexes

How to Disable FileServer Directory Listings
https://www.alexedwards.net/blog/disable-http-fileserver-directory-listings

Organising database access in Go
https://www.alexedwards.net/blog/organising-database-access

The Twelve-Factor App
https://12factor.net/config
https://12factor.net/

jmoiron/sqlx
sqlx is a library which provides a set of extensions on go's standard database/sql library.
https://github.com/jmoiron/sqlx

blockloop/scan
Scan standard lib database rows directly to structs or slices.
https://github.com/blockloop/scan

Which Go router should I use?
https://www.alexedwards.net/blog/which-go-router-should-i-use

<!-- --------------------------------------------------------------- -->

