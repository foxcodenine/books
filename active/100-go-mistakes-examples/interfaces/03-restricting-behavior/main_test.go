package main

import (
	"bytes"
	"testing"
)

func TestQueueMonitorCheck(t *testing.T) {

	limit := 10

	threshold := &Threshold{}
	threshold.Set(limit)

	monitor := NewQueueMonitor(threshold)

	var buf bytes.Buffer

	monitor.Check(&buf, 3)

	want := "queue ok: 3 <= 10"
	if buf.String() != want {
		t.Errorf("got %q, want %q", buf.String(), want)
	}

	buf.Reset()

	monitor.Check(&buf, 12)

	want = "queue too long: 12 > 10"
	if buf.String() != want {
		t.Errorf("got %q, want %q", buf.String(), want)
	}
}
