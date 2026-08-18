package main

import (
	"fmt"
	"io"
	"os"
	"sync"
	"time"
)

// -------------------------------------------------------------------------------------------------

// PrintTicker prints every tick until done is closed.
func PrintTicker(wg *sync.WaitGroup, w io.Writer, ticks <-chan time.Time, done <-chan struct{}) {
	defer wg.Done()

	for {
		select {
		case t := <-ticks:
			fmt.Fprintln(w, t.Format(time.RFC3339))

		case <-done:
			return
		}
	}
}

// -------------------------------------------------------------------------------------------------

func main() {
	ticker := time.NewTicker(2 * time.Second)
	defer ticker.Stop() // a ticker that is never stopped keeps its runtime resources

	timer := time.NewTimer(11 * time.Second)
	defer timer.Stop()

	done := make(chan struct{})

	var wg sync.WaitGroup
	wg.Add(1)
	go PrintTicker(&wg, os.Stdout, ticker.C, done)

	<-timer.C

	close(done) // signal the goroutine to return...
	wg.Wait()   // ...and wait for it, so main does not exit mid-print
}
