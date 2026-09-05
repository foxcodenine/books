package main

import (
	"fmt"
	"io"
)

// -----------------------------------------------------------------------------

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

type thresholdReader interface {
	Get() int
}

// -----------------------------------------------------------------------------

type QueueMonitor struct {
	threshold thresholdReader
}

func (qm *QueueMonitor) Check(w io.Writer, queueLenght int) {

	threshold := qm.threshold.Get()

	if queueLenght > threshold {
		fmt.Fprintf(w, "queque too long: %d > %d ", queueLenght, threshold)
		return
	}

	fmt.Fprintf(w, "queque okay: %d <= %d ", queueLenght, threshold)
}

func NewQueueMonitor(threshold thresholdReader) QueueMonitor {
	return QueueMonitor{
		threshold: threshold,
	}
}

// -----------------------------------------------------------------------------
