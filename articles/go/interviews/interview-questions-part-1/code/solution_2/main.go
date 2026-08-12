package main

import (
	"fmt"
	"sync"
)

// Interviewer: What will happen when the code is compiled, what will the line
// fmt.Println(*value) output, and how can we fix all errors?

func main() {

	// -----------------------------------------------------------------

	ch := make(chan *int, 4)

	array := []int{1, 2, 3}

	wg := sync.WaitGroup{}

	wg.Add(len(array))

	// -----------------------------------------------------------------

	go func() {

		for _, value := range array {
			ch <- &value
		}

	}()

	// -----------------------------------------------------------------

	go func() {
		for value := range ch {

			fmt.Println(*value)
			wg.Done()
		}

	}()

	wg.Wait()
	// The channel remains open, so this is not ideal for a long-running program.

}
