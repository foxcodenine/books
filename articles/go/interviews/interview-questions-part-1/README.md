# Go Interview Questions: Pointers, Channels, and Range

- Source: https://medium.com/@ninucium/go-interview-questions-part-1-pointers-channels-and-range-67c61345cf3c
- Author: Nina Pakshina
- Status: Completed
- Accessed: 2026-08-12

## Goal

Understand pointers to range variables, closing channels, and waiting for goroutines.

## Notes

- `question/` deadlocks because the channel is never closed.
- `solution_1/` closes the channel. In Go 1.22+, each range iteration has its own variable.
- `solution_2/` waits for a known number of received values without closing the channel.

## Code

Run the working solutions:

```bash
cd code
go run ./solution_1
go run ./solution_2
```
