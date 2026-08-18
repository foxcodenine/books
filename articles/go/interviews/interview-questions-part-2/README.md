# Go Interview Questions, Part 2: Slices

- Source: https://medium.com/@ninucium/go-interview-questions-part-2-slices-87f5289fb7eb
- Author: Nina Pakshina
- Status: In progress
- Accessed: 2026-08-12

## Goal

Understand slice length, capacity, growth, and shared backing arrays.

## Notes

- `example-1/` shows how capacity grows as values are appended.
- `example-2/` shows that slices remain connected when an append fits within capacity.
- `example-3/` shows that exceeding capacity gives one slice a new backing array.
- Exact capacity growth can vary because of runtime allocation and compiler optimization.

## Code

Run the examples from this directory:

```bash
go run ./code/example-1/main.go
go run ./code/example-2/main.go
go run ./code/example-3/main.go
```
