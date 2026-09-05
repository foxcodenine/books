package main

// -----------------------------------------------------------------------------

// Customer is the data we want to save.
type Customer struct {
	ID string
}

// -----------------------------------------------------------------------------

// CustomerStorer says WHAT we need ("something that can store a customer"),
// not HOW it's done. No mention of SQL, files, memory, etc.
type CustomerStorer interface {
	StoreCustomer(Customer) error
	DeleteCustomer(string) error
	ListCustomers() ([]Customer, error)
}

// -----------------------------------------------------------------------------

// CustomerService holds the interface, not a concrete type.
// That's the decoupling: it doesn't know or care who actually stores the data.
type CustomerService struct {
	store CustomerStorer
}

// -----------------------------------------------------------------------------

// NewCustomerService lets the caller decide the real implementation
// (a real DB in production, a fake one in tests).
func NewCustomerService(store CustomerStorer) CustomerService {
	return CustomerService{
		store: store,
	}
}

// -----------------------------------------------------------------------------

// CreateNewCustomer does the business logic, then hands the customer
// to whatever storer it was given.
func (cs *CustomerService) CreateNewCustomer(id string) error {
	customer := Customer{
		ID: id,
	}

	return cs.store.StoreCustomer(customer)
}

func (cs *CustomerService) DeleteCustomer(id string) error {
	return cs.store.DeleteCustomer(id)
}

func (cs *CustomerService) ListCustomers() ([]Customer, error) {
	return cs.store.ListCustomers()
}
