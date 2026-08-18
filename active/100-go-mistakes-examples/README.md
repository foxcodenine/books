# 100 Go Mistakes Examples

Personal examples and tests based on lessons from *100 Go Mistakes and How to Avoid Them*.

## Topics

- [Using `io.Reader` and `io.Writer`](interfaces/01-reader-writer/)
- [Decoupling code with interfaces](interfaces/02-decoupling/)
- [Restricting behavior with small interfaces](interfaces/03-restricting-behavior/)
- [Stopping tickers and shutting down goroutines](time/01-ticker-timer/)

## Verification

```bash
go test ./...
go vet ./...
```
