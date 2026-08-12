go mod init snippetbox.letsgo.foxcodenine

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
