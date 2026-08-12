package main

import "fmt"

func printSlice(label string, x []int) {
	fmt.Printf("%-18s len=%-2d cap=%-2d x=%v\n", label, len(x), cap(x), x)
}

func main() {
	// With Go 1.26, passing x to fmt makes this example use heap growth.
	// Below capacity 256, the growth formula doubles when more space is needed.
	// Allocator rounding can still make the observed capacity different.
	var x []int
	printSlice("initial", x)

	// No capacity exists, so append allocates enough space for the new element.
	x = append(x, 1)
	printSlice("append 1", x)

	// The required length exceeds capacity, so a larger backing array is allocated.
	x = append(x, 2, 3, 4)
	printSlice("append 2,3,4", x)

	// Length exceeds capacity; here capacity doubles from 4 to 8.
	x = append(x, 5)
	printSlice("append 5", x)

	// Length exceeds capacity again; here it doubles from 8 to 16.
	x = append(x, 6, 7, 8, 9)
	printSlice("append 6..9", x)

	// Here capacity grows from 16 to 32.
	x = append(x, 10, 11, 12, 13, 14, 15, 16, 17, 18)
	printSlice("append 10..18", x)

	// A non-escaping stack slice may grow differently due to compiler optimization.
}
