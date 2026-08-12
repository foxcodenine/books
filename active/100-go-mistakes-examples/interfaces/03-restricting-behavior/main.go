package main

import (
	"fmt"
	"io"
	"os"
)

// -------------------------------------------------------------------------------------------------

// Threshold is the full type: it can be read AND changed.
type Threshold struct {
	value int
}

func (t *Threshold) Get() int {
	return t.value
}

func (t *Threshold) Set(value int) {
	t.value = value
}

// -------------------------------------------------------------------------------------------------

// thresholdReader is the restricted view: read only, no Set.
// It lives here, next to the code that consumes it, not next to Threshold.
type thresholdReader interface {
	Get() int
}

// -------------------------------------------------------------------------------------------------

type QueueMonitor struct {
	threshold thresholdReader
}

func NewQueueMonitor(threshold thresholdReader) QueueMonitor {
	return QueueMonitor{
		threshold: threshold,
	}
}

func (m QueueMonitor) Check(w io.Writer, queueLength int) {
	threshold := m.threshold.Get()

	if queueLength > threshold {
		fmt.Fprintf(w, "queue too long: %d > %d", queueLength, threshold)
		return
	}

	fmt.Fprintf(w, "queue ok: %d <= %d", queueLength, threshold)

	// This would NOT compile:
	//
	// m.threshold.Set(100)
	//
	// because thresholdReader only exposes Get().
}

// -------------------------------------------------------------------------------------------------

func main() {
	threshold := &Threshold{}
	threshold.Set(10)

	monitor := NewQueueMonitor(threshold)

	monitor.Check(os.Stdout, 10)
	monitor.Check(os.Stdout, 42)
}
