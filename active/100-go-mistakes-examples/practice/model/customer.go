package model

type Customer struct {
	ID int
}

// -----------------------------------------------------------------------------

type CustomerStorer interface {
	StoreCustomer(Customer) error
	DeleteCustomer(ID int) error
}

// -----------------------------------------------------------------------------

type CustomerService struct {
	store CustomerStorer
}

func (cs *CustomerService) CreateNewCustomer(id int) error {
	var customer Customer
	customer.ID = id

	cs.store.StoreCustomer(customer)

	return nil
}

// -----------------------------------------------------------------------------

func NewCustomerService(store CustomerStorer) CustomerService {

	return CustomerService{
		store: store,
	}
}
