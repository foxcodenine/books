package main

import "testing"

// -------------------------------------------------------------------------------------------------

type FakeStore struct {
	SavedCustomer Customer
}

func (f *FakeStore) StoreCustomer(customer Customer) error {
	f.SavedCustomer = customer
	return nil
}

// -------------------------------------------------------------------------------------------------

func TestCreateNewCustomer(t *testing.T) {

	store := &FakeStore{}

	service := NewCustomerService(store)

	err := service.CreateNewCustomer("123")
	if err != nil {
		t.Fatal(err)
	}

	if store.SavedCustomer.ID != "123" {
		t.Errorf("expected 123, got %s", store.SavedCustomer.ID)
	}
}

// -------------------------------------------------------------------------------------------------
