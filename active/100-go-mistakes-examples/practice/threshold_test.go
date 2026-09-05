package main

import (
	"bytes"
	"fmt"
	"testing"
)

func TestQueueMonitorCheck(t *testing.T) {

	value := 10

	threshold := Threshold{
		value: value,
	}
	queueMonitor := NewQueueMonitor(&threshold)

	// -----------------------------------------------------------------

	queueLenght := 5

	want := fmt.Sprintf("queque okay: %d <= %d ", queueLenght, value)

	output := bytes.Buffer{}

	queueMonitor.Check(&output, queueLenght)

	got := output.String()

	if got != want {
		t.Errorf("got %q, want %q", got, want)
	}
	// -----------------------------------------------------------------

	queueLenght = 15

	want = fmt.Sprintf("queque too long: %d > %d ", queueLenght, value)

	output = bytes.Buffer{}

	queueMonitor.Check(&output, queueLenght)

	got = output.String()

	if got != want {
		t.Errorf("got %q, want %q", got, want)
	}

}
