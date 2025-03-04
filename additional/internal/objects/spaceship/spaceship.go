package spaceship

import (
	"additional/internal/models/angle"
	"additional/internal/models/vector"
)

type Spaceship struct {
	alpha           angle.Angle
	angularVelocity int
	fuel            int
	rateOfFlow      int
	velocity        vector.Vector
	position        vector.Vector
}

func NewSpaceship(a angle.Angle, av int, f int, rof int, v vector.Vector, p vector.Vector) *Spaceship {
	return &Spaceship{alpha: a, angularVelocity: av, fuel: f, rateOfFlow: rof, velocity: v, position: p}
}

func (s *Spaceship) GetAngle() (int, error) {
	return s.alpha.Value, nil
}

func (s *Spaceship) SetAngle(newValue int) error {
	s.alpha.Value = newValue
	return nil
}

func (r *Spaceship) GetDivision() (int, error) {
	return r.alpha.Division, nil
}

func (s *Spaceship) GetAngularVelocity() (int, error) {
	return s.angularVelocity, nil
}

func (s *Spaceship) GetVelocity() (vector.Vector, error) {
	return s.velocity, nil
}

func (s *Spaceship) SetVelocity(value vector.Vector) error {
	s.velocity = value
	return nil
}

func (s *Spaceship) GetPosition() (vector.Vector, error) {
	return s.position, nil
}

func (s *Spaceship) SetPosition(newVector vector.Vector) error {
	s.position = newVector
	return nil
}

func (s *Spaceship) GetFuel() (int, error) {
	return s.fuel, nil
}

func (s *Spaceship) SetFuel(newValue int) error {
	s.fuel = newValue
	return nil
}

func (s *Spaceship) GetRateOfFlow() (int, error) {
	return s.rateOfFlow, nil
}

func (s *Spaceship) CheckFuel() bool {
	return s.fuel > 0
}
