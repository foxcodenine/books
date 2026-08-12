package main

import (
	"log/slog"
)

// -------------------------------------------------------------------------------------------------
type MySQLSore struct{}

func (s *MySQLSore) StoreCustomer(customer Customer) error {
	slog.Info("Saving customer", "id", customer.ID)
	return nil
}

// -------------------------------------------------------------------------------------------------

func main() {
	store := MySQLSore{}

	service := NewCustomerService(&store)

	err := service.CreateNewCustomer("123")

	if err != nil {
		slog.Error("Unable to create new customer", "error", err)
	}
}
