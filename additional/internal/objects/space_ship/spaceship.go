package spaceship

import (
	"additional/internal/models/angle"
)

type Spaceship struct {
	alpha           angle.Angle
	angularVelocity int
}

func (s *Spaceship) GetAngle() int {
	return s.alpha.Value
}

func (s *Spaceship) SetAngle(newValue int) error {
	s.alpha.Value = newValue
	return nil
}

func (r *Spaceship) GetDivision() int {
	return r.alpha.Division
}

func (s *Spaceship) GetAngularVelocity() int {
	return s.angularVelocity
}
