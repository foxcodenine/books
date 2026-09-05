# Stopping tickers and shutting down goroutines

## Purpose

This exercise shows how to stop time-based work and shut down a goroutine cleanly.

The ticker produces repeated events, the timer decides when to stop, the `done` channel signals the goroutine, and the `WaitGroup` waits for it to finish.

## Exercise

Write a `package main` program that prints a timestamp every 2 seconds for about 10 seconds, then exits cleanly.

Requirements:

1. Create a ticker with `time.NewTicker` and a timer with `time.NewTimer`.
2. Write a function `PrintTicker` that runs in a goroutine and prints each tick, formatted with `time.RFC3339`.
   - It must receive the **tick channel** (`<-chan time.Time`), not the `*time.Ticker` — the consumer only needs to read ticks.
   - It must write to an `io.Writer` parameter, not call `fmt.Println` directly.
   - It must stop when a `done` channel is closed. Use `select`.
3. `main` waits on the timer's channel, then closes `done`.
4. No leaks: the ticker and timer must be stopped, and `main` must not exit before the goroutine has finished — use a `sync.WaitGroup`.

Then answer, without looking:

- What happened if wg.Wait() is removed?
   > main could exit before the goroutine has finished shutting down

- What actually happens if you send the `*time.Ticker` over a channel instead of its `C` field?
   > *time.Ticker is the ticker object; ticker.C is the channel that emits time.Time values. 
      My function only needs the channel, so I pass ticker.C

- What leaks if you drop the `done` channel? What leaks if you drop `ticker.Stop()`?
   > the goroutine would keep waiting for ticks and never return

- Why is the timer set to 11s rather than 10s?
   > the timer is set to 11s so the ticker has time to produce and print the tick at 10s.

## Verification

```bash
gofmt -l .
go vet ./...
go run .
```
