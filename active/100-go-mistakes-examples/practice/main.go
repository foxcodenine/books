package main

import "os"

func main() {

	var threshold Threshold
	threshold.Set(10)

	monitor := NewQueueMonitor(&threshold)

	monitor.Check(os.Stdout, 5)

	monitor.Check(os.Stdout, 15)
}
