package models

import "database/sql"

type ExampleModel struct {
	DB *sql.DB
}

func (m *ExampleModel) ExampleTransaction() error {
	// Start a new transaction.
	tx, err := m.DB.Begin()
	if err != nil {
		return err
	}

	// Ensure rollback if commit doesn’t happen.
	defer tx.Rollback()

	// Run first query inside the transaction.
	_, err = tx.Exec("INSERT INTO ...")
	if err != nil {
		return err
	}

	// Run second query inside the transaction.
	_, err = tx.Exec("UPDATE ...")
	if err != nil {
		return err
	}

	// Commit all changes.
	return tx.Commit()

	// NOTE:  You must always call either Rollback() or Commit().
	// If you don’t the connection will stay open and not be returned to the connection pool.
}

func (m *ExampleModel) InsertUsers(users []string) error {
	// Prepare parses the SQL once and returns a statement object.
	// Useful when running the same query many times (better performance).
	stmt, err := m.DB.Prepare("INSERT INTO users (name) VALUES (?)")
	if err != nil {
		return err
	}
	// Close statement when done to free resources.
	defer stmt.Close()

	// Now we can reuse the prepared statement in a loop.
	for _, name := range users {
		// Exec runs the already-prepared statement with given parameters.
		// Avoids re-parsing SQL every time, unlike DB.Exec in a loop.
		_, err = stmt.Exec(name)
		if err != nil {
			return err
		}
	}

	// Return nil if all inserts succeed.
	return nil
}
