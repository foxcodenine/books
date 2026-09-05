# Decoupling with an Interface

## Purpose

This exercise shows how an interface can separate business logic from storage code.

`CustomerService` depends on the behavior described by `CustomerStorer`, not on a specific store. This makes the storage replaceable and the service easier to test.

## Exercise

Create a program that saves, deletes, and lists customers without making the customer service depend on a specific storage system.

## Requirements

1. Create a `Customer` type with an `ID` field.
2. Create a small `CustomerStorer` interface with this behavior:

```go
StoreCustomer(Customer) error
DeleteCustomer(string) error
ListCustomers() ([]Customer, error)
```

3. Create a `CustomerService` that stores a `CustomerStorer`.
4. Write a `NewCustomerService` constructor.
5. Write a `CreateNewCustomer` method that:
   - receives a customer ID
   - creates a `Customer`
   - asks the store to save it
6. Write a `DeleteCustomer` method that asks the store to delete a customer.
7. Write a `ListCustomers` method that returns the customers from the store.
8. Create a storage implementation for the main program.
9. Create a fake storage implementation for the tests.
10. Verify that the service creates, deletes, and lists customers through the fake store.

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
- Why should `ListCustomers` return customers instead of printing them?

## Test

Write tests that:

1. Verify that `CreateNewCustomer` sends the correct customer to the fake store.
2. Verify that `DeleteCustomer` sends the correct ID to the fake store.
3. Verify that `ListCustomers` returns the customers supplied by the fake store.

## Verification

```bash
gofmt -l .
go vet .
go test .
go run .
```

## Main lesson

Depend on the behavior you need, not on a specific implementation.
