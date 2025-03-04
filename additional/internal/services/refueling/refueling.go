// пакет отвечает за работу с топливом
package refuel

import (
	"errors"
)

type IRefuel interface {
	GetFuel() (int, error)
	SetFuel(value int) error
	GetRateOfFlow() (int, error)
	CheckFuel() bool
}

type Refueling struct {
	fuel       int
	rateOfFlow int
}

func NewRefueling(fuel int, rateOfFlow int) *Refueling {
	return &Refueling{fuel: fuel, rateOfFlow: rateOfFlow}
}

func (r *Refueling) GetFuel() (int, error) {
	return r.fuel, nil
}

func (r *Refueling) SetFuel(newValue int) error {
	if newValue < 0 {
		return errors.New("fuel value cannot be negative")
	}
	r.fuel = newValue
	return nil
}

func (r *Refueling) GetRateOfFlow() (int, error) {
	return r.rateOfFlow, nil
}

func (r *Refueling) CheckFuel() bool {
	return r.fuel > 0
}
