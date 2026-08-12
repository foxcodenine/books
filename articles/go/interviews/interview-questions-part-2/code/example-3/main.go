package main

import "fmt"

func printSlice(label string, x []int) {
	fmt.Printf(
		"%-10s len=%d cap=%d address=%p values=%v\n",
		label,
		len(x),
		cap(x),
		&x[0],
		x,
	)
}

func main() {
	x := []int{1, 2, 3}
	y := x

	// x and y initially share the same backing array.
	printSlice("x before", x)
	printSlice("y before", y)

	// x has no spare capacity, so append allocates a new backing array.
	x = append(x, 4)

	// This change now affects only x.
	x[0] = 0

	printSlice("x after", x)
	printSlice("y after", y)
}
