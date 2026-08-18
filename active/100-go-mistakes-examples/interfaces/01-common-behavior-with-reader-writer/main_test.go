package main

import (
	"strings"
	"testing"
)

func TestCopySourceToDest(t *testing.T) {

	input := "Hello Chris"

	source := strings.NewReader(input)
	var dest strings.Builder

	err := copySourceToDest(source, &dest)

	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}

	if dest.String() != input {
		t.Errorf("got %q, want %q", dest.String(), input)
	}
}
