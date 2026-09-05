package main

import (
	"fmt"
	"log/slog"
	"slices"
)

// -------------------------------------------------------------------------------------------------
type MemoryStore struct {
	customers []Customer
}

func (s *MemoryStore) StoreCustomer(customer Customer) error {
	s.customers = append(s.customers, customer)
	slog.Info("customer saved", "id", customer.ID)
	return nil
}

func (s *MemoryStore) DeleteCustomer(id string) error {
	for i, customer := range s.customers {
		if customer.ID == id {
			s.customers = append(s.customers[:i], s.customers[i+1:]...)
			slog.Info("customer deleted", "id", id)
			return nil
		}
	}

	return fmt.Errorf("customer with ID %s does not exist", id)
}

func (s *MemoryStore) ListCustomers() ([]Customer, error) {
	return slices.Clone(s.customers), nil
}

// -------------------------------------------------------------------------------------------------

func main() {
	store := MemoryStore{}

	service := NewCustomerService(&store)

	if err := service.CreateNewCustomer("123"); err != nil {
		slog.Error("Unable to create new customer", "error", err)
		return
	}

	customers, err := service.ListCustomers()
	if err != nil {
		slog.Error("Unable to list customers", "error", err)
		return
	}

	for _, customer := range customers {
		slog.Info("customer", "id", customer.ID)
	}

	if err := service.DeleteCustomer("123"); err != nil {
		slog.Error("Unable to delete customer", "error", err)
	}
}
