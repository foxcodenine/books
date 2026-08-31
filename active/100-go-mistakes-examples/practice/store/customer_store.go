package store

import "github.com/foxcodenine/100-go-mistakes-examples/practice/model"

type CustomerStore struct {
	customer []model.Customer
}

func (cs *CustomerStore) StoreCustomer(c model.Customer) error {

}
