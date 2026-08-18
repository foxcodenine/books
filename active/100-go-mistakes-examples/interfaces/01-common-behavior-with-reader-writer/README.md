# Common behavior with interfaces

## Exercise

Write a `package main` program that copies data from a source to a destination using the common behavior provided by Go's `io.Reader` and `io.Writer` interfaces.

Requirements:

1. Write a function called `copySourceToDest`.
2. The function must receive:
   - an `io.Reader` as the source
   - an `io.Writer` as the destination
3. Do **not** make the function depend directly on `strings.Reader` or `strings.Builder`.
4. Create a small byte buffer and repeatedly:
   - read data from the source
   - write the bytes that were read to the destination
5. Handle:
   - successful reads
   - write errors
   - `io.EOF`
   - other read errors
6. In `main`:
   - create a source using `strings.NewReader`
   - create a destination using `strings.Builder`
   - call `copySourceToDest`
   - print/log the final copied value
7. Write a unit test that:
   - copies `"Hello Chris"`
   - verifies that no error occurred
   - verifies that the destination contains exactly `"Hello Chris"`

## Questions

Then answer, without looking:

- What is the purpose of `io.Reader` in this example?

- What is the purpose of `io.Writer`?

- Why does `copySourceToDest` accept `io.Reader` instead of `*strings.Reader`?

- Why does it accept `io.Writer` instead of `*strings.Builder`?

- What is the **common behavior** represented by `io.Reader`?

- What is the **common behavior** represented by `io.Writer`?

- Does `copySourceToDest` need to know the concrete type of `source`?

- Does `copySourceToDest` need to know the concrete type of `dest`?

- Why can `strings.Reader` be passed as an `io.Reader`?

- Why can `*strings.Builder` be passed as an `io.Writer`?

- In Go, do we explicitly declare that `strings.Reader` implements `io.Reader`?

- What does this line do?

```go
n, err := source.Read(buffer)
```

- What does `n` represent?

- Why do we write:

```go
buffer[:n]
```

instead of:

```go
buffer
```

- What does `io.EOF` mean?

- Why do we check `n > 0` before checking `io.EOF`?

- If tomorrow the source changes from a string to a file, should `copySourceToDest` have to change?

- If tomorrow the destination changes from a `strings.Builder` to a file, should `copySourceToDest` have to change?

- Why does using `io.Reader` and `io.Writer` make this function more reusable?

- How does this example demonstrate the idea of **common behavior**?

## Test

The test should verify the behavior of the function rather than its concrete implementation.

```go
func TestCopySourceToDest(t *testing.T) {
	input := "Hello Chris"

	source := strings.NewReader(input)
	var dest strings.Builder

	err := copySourceToDest(source, &dest)

	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}

	if dest.String() != input {
		t.Errorf("got %q, want %q", dest.String(), input)
	}
}
```

## Verification

```bash
gofmt -l .
go vet ./...
go test ./...
go run .
```