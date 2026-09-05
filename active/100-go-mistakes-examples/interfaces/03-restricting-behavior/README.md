# Restricting Behavior with a Small Interface

## Purpose

This exercise shows how a small interface can limit the behavior available to some code.

`Threshold` can be read and changed, but `QueueMonitor` receives a `thresholdReader` that only provides `Get`. The monitor can read the threshold but cannot change it.

## Exercise

Create a queue monitor that can read a threshold but cannot change it.

## Requirements

1. Create a `Threshold` type that stores an integer value.
2. Add a `Get` method that returns the value.
3. Add a `Set` method that changes the value.
4. Create a small `thresholdReader` interface containing only:

```go
Get() int
```

5. Create a `QueueMonitor` that stores a `thresholdReader`.
6. Write a `NewQueueMonitor` constructor.
7. Write a `Check` method on the `QueueMonitor` that:
   - receives an `io.Writer`
   - receives the current queue length
   - reads the threshold
   - reports whether the queue is too long
8. In `main`, create a threshold and pass it to the monitor.

## Questions

Answer these without looking at the solution:

- Why does `Threshold` have both `Get` and `Set`?
- Why does `thresholdReader` contain only `Get`?
- Can `QueueMonitor` call `Set` through the interface?
- Why is the interface defined near `QueueMonitor`?
- How does the interface restrict behavior?
- Why does `Check` accept an `io.Writer`?
- Could a different threshold type be passed to `NewQueueMonitor`?
- What methods would that type need?

## Test

Write a test that:

1. Creates a threshold with a value of `10`.
2. Creates a `QueueMonitor`.
3. Checks a queue length below the threshold.
4. Checks a queue length above the threshold.
5. Verifies both messages using a `bytes.Buffer`.

## Verification

```bash
gofmt -l .
go vet .
go test .
go run .
```

## Main lesson

Give code access to only the behavior it needs.
