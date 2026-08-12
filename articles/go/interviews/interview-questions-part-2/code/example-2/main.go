package main

import "fmt"

func printSlice(label string, x []int) {
	fmt.Printf("%-18s len=%d cap=%d x=%v\n", label, len(x), cap(x), x)
}

func main() {
	// A slice literal starts with len=1 and cap=1 here.
	x := []int{1}
	printSlice("initial x", x)

	// Capacity is full, so Go grows it from 1 to 2.
	x = append(x, 2)
	printSlice("append 2", x)

	// Capacity is full again, so the small-slice formula doubles it to 4.
	x = append(x, 3)
	printSlice("append 3", x)

	// Both slices now share the same backing array with one spare position.
	y := x
	printSlice("copy to y", y)

	// The new element fits, so x grows in length without changing capacity.
	x = append(x, 4)
	x[0] = 0

	printSlice("final x", x)
	printSlice("final y", y)

	// y still shares the array; its shorter length only hides the fourth element.
	fmt.Println("y extended:", y[:4])

	// Runtime rounding and compiler optimization can change observed capacities.
}
