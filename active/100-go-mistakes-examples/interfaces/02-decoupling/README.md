# Decoupling with an Interface

## Exercise

Create a program that saves a customer without making the customer service depend on a specific storage system.

## Requirements

1. Create a `Customer` type with an `ID` field.
2. Create a small `CustomerStorer` interface with this behavior:

```go
StoreCustomer(Customer) error
```

3. Create a `CustomerService` that stores a `CustomerStorer`.
4. Write a `NewCustomerService` constructor.
5. Write a `CreateNewCustomer` method that:
   - receives a customer ID
   - creates a `Customer`
   - asks the store to save it
6. Create a storage implementation for the main program.
7. Create a fake storage implementation for the test.
8. Verify that the fake store receives the correct customer.

## Questions

Answer these without looking at the solution:

- What behavior does `CustomerStorer` describe?
- Why does `CustomerService` depend on the interface?
- Does `CustomerService` know how the customer is stored?
- Could the storage change from MySQL to a file without changing the service?
- Why is a fake store useful in the test?
- Where should the interface be defined: near the code that uses it or near the implementation?
- Why should the interface contain only the method the service needs?
- How does this interface decouple the service from the storage?

## Test

Write a test that:

1. Creates a fake store.
2. Passes it to `NewCustomerService`.
3. Calls `CreateNewCustomer` with `"123"`.
4. Checks that no error occurred.
5. Checks that the saved customer ID is `"123"`.

## Verification

```bash
gofmt -l .
go vet .
go test .
go run .
```

## Main lesson

Depend on the behavior you need, not on a specific implementation.
