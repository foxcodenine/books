package main

import (
	"io"
	"log/slog"
	"strings"
)

func copySourceToDest(source io.Reader, dest io.Writer) error {

	buffer := make([]byte, 4)

	for {
		n, err := source.Read(buffer)

		if n > 0 {
			_, writeErr := dest.Write(buffer[:n])

			if writeErr != nil {
				return writeErr
			}
		}

		if err == io.EOF {
			return nil
		}

		if err != nil {
			return err
		}
	}
}

// -------------------------------------------------------------------------------------------------

func main() {
	source := strings.NewReader("Hello Chris")

	var dest strings.Builder

	err := copySourceToDest(source, &dest)

	if err != nil {
		slog.Error("failed to copy source to destination", "error", err)
		return
	}

	slog.Info(dest.String())
}
