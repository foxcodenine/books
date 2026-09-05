package main

import "os"

func main() {
	threshold := &Threshold{}
	threshold.Set(10)

	monitor := NewQueueMonitor(threshold)

	monitor.Check(os.Stdout, 10)
	monitor.Check(os.Stdout, 42)
}
