package main

import (
	"fmt"
	"io"
)

// Threshold is the full type: it can be read and changed.
type Threshold struct {
	value int
}

func (t *Threshold) Get() int {
	return t.value
}

func (t *Threshold) Set(value int) {
	t.value = value
}

// -----------------------------------------------------------------------------

// thresholdReader is the restricted view.
// It allows reading the threshold but not changing it.
type thresholdReader interface {
	Get() int
}

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

	// This would not compile:
	//
	// m.threshold.Set(100)
	//
	// thresholdReader only provides Get.
}
