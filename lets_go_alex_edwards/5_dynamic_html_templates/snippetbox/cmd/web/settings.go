package main

import (
	"database/sql"
	"fmt"
	"os"

	_ "github.com/go-sql-driver/mysql"
	"github.com/joho/godotenv"
)

var envPath = "./"
var envFilename = ".env"

// LoadEnv loads environment variables from a .env file if not running in Docker.
func loadEnv() error {
	os.Setenv("TZ", "UTC")

	fullPath := fmt.Sprintf("%s%s", envPath, envFilename)

	err := godotenv.Load(fullPath)

	if err != nil {
		return err
	}

	return nil
}

// The openDB() function wraps sql.Open() and returns a sql.DB connection pool
// for a given DSN.
func openDB(dsn string) (*sql.DB, error) {
	db, err := sql.Open("mysql", dsn)
	if err != nil {
		return nil, err
	}

	if err = db.Ping(); err != nil {
		return nil, err
	}

	return db, nil
}
