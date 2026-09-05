package main

import (
	"bytes"
	"testing"
)

func TestQueueMonitorCheck(t *testing.T) {
	threshold := &Threshold{}
	threshold.Set(10)

	monitor := NewQueueMonitor(threshold)

	var output bytes.Buffer

	monitor.Check(&output, 3)

	want := "queue ok: 3 <= 10"
	if output.String() != want {
		t.Errorf("got %q, want %q", output.String(), want)
	}

	output.Reset()

	monitor.Check(&output, 12)

	want = "queue too long: 12 > 10"
	if output.String() != want {
		t.Errorf("got %q, want %q", output.String(), want)
	}
}
