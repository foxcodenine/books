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

	wg.Add(1)

	// -----------------------------------------------------------------

	go func() {

		for _, value := range array {
			ch <- &value
		}

	}()

	// -----------------------------------------------------------------

	go func() {
		for value := range ch {

			fmt.Println(*value) // what will be printed here?
		}

		wg.Done()
	}()

	wg.Wait()

}
