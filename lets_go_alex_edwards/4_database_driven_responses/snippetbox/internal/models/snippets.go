package models

import (
	"database/sql"
	"errors"
	"time"
)

// Define a Snippet type to hold the data for an individual snippet
type Snippet struct {
	ID      int
	Title   string
	Content string
	Created time.Time
	Expires time.Time
}

// Define a SnippetModel type which wraps a sql.DB connection pool
type SnippetModel struct {
	DB *sql.DB
}

// Insert a new snippet into the database and return its ID
func (m *SnippetModel) Insert(title, content string, expires int) (int, error) {

	stmt := `INSERT INTO snippets (title, content, created, expires)
	VALUES(?, ?, UTC_TIMESTAMP(), DATE_ADD(UTC_TIMESTAMP(), INTERVAL ? DAY))`

	result, err := m.DB.Exec(stmt, title, content, expires)
	if err != nil {
		return 0, err
	}

	id, err := result.LastInsertId()
	if err != nil {
		return 0, err
	}

	// NOTE:  DB.Exec() retuen a sql.Result type, wich have two methods:
	// 		LastInsertId()
	// 		RowsAffected()
	// Important - Not all DB drivers support these methods

	return int(id), nil
}

// Return a specific snippet based on its id
func (m *SnippetModel) Get(id int) (*Snippet, error) {

	stmt := `SELECT id, title, content, created, expires FROM snippets
			WHERE expires > UTC_TIMESTAMP() AND id = ?`

	// This returns a pointer to a sql.Row object which
	// holds the result from the database.
	row := m.DB.QueryRow(stmt, id)

	//  Initialize a pointer to a new zeroed Snippet struct
	s := &Snippet{}

	// Use row.Scan() to copy the values from each field in sql.Row to the
	// corresponding field in the Snippet struct.
	err := row.Scan(&s.ID, &s.Title, &s.Content, &s.Created, &s.Expires)

	if err != nil {

		if errors.Is(err, sql.ErrNoRows) {
			return nil, ErrNoRecord
		} else {
			return nil, err
		}
	}

	// If everything went OK then return the Snippet object.
	return s, nil
}

// Return the 10 most recently created snippets.
func (m *SnippetModel) Latest() ([]*Snippet, error) {
	// SQL query to get latest 10 non-expired snippets.
	stmt := `SELECT id, title, content, created, expires FROM snippets
             WHERE expires > UTC_TIMESTAMP() ORDER BY id DESC LIMIT 10`

	// Run the query.
	rows, err := m.DB.Query(stmt)
	if err != nil {
		return nil, err
	}
	// Ensure rows are closed later.
	defer rows.Close()

	// Slice to hold results.
	snippets := []*Snippet{}

	// Iterate through rows.
	for rows.Next() {
		s := &Snippet{} // New snippet.

		// Copy row values into struct.
		err = rows.Scan(&s.ID, &s.Title, &s.Content, &s.Created, &s.Expires)
		if err != nil {
			return nil, err
		}

		snippets = append(snippets, s) // Add to slice.
	}

	// Check for errors during iteration.
	if err = rows.Err(); err != nil {
		return nil, err
	}

	// Return results.
	return snippets, nil
}
