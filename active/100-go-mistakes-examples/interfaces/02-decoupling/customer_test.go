package main

import (
	"slices"
	"testing"
)

// -------------------------------------------------------------------------------------------------

type FakeStore struct {
	SavedCustomer Customer
	DeletedID     string
	Customers     []Customer
}

func (f *FakeStore) StoreCustomer(customer Customer) error {
	f.SavedCustomer = customer
	return nil
}

func (f *FakeStore) DeleteCustomer(id string) error {
	f.DeletedID = id
	return nil
}

func (f *FakeStore) ListCustomers() ([]Customer, error) {
	return f.Customers, nil
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

func TestDeleteCustomer(t *testing.T) {
	store := &FakeStore{}
	service := NewCustomerService(store)

	err := service.DeleteCustomer("123")
	if err != nil {
		t.Fatal(err)
	}

	if store.DeletedID != "123" {
		t.Errorf("expected 123, got %s", store.DeletedID)
	}
}

func TestListCustomers(t *testing.T) {
	want := []Customer{{ID: "123"}, {ID: "456"}}
	store := &FakeStore{Customers: want}
	service := NewCustomerService(store)

	got, err := service.ListCustomers()
	if err != nil {
		t.Fatal(err)
	}

	if !slices.Equal(got, want) {
		t.Errorf("got %v, want %v", got, want)
	}
}

// -------------------------------------------------------------------------------------------------
