package rotating

import (
	"additional/internal/models/angle"
)

type IRotable interface {
	GetAngle() (int, error)
	SetAngle(value int) error
	GetDivision() (int, error)
	GetAngularVelocity() (int, error)
}

type Rotable struct {
	alpha           angle.Angle
	angularVelocity int
}

func NewRotatable(alpha angle.Angle, angularVelocity int) *Rotable {
	return &Rotable{alpha: alpha, angularVelocity: angularVelocity}
}

func (r *Rotable) GetAngle() (int, error) {
	return r.alpha.Value, nil
}

func (r *Rotable) SetAngle(newValue int) error {
	r.alpha.Value = newValue
	return nil
}

func (r *Rotable) GetDivision() (int, error) {
	return r.alpha.Division, nil
}

func (r *Rotable) GetAngularVelocity() (int, error) {
	return r.angularVelocity, nil
}
