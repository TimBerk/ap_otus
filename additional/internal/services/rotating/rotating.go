package rotating

import (
	"additional/internal/models/angle"
)

type IRotable interface {
	GetAngle() int
	SetAngle(value int) error
	GetDivision() int
	GetAngularVelocity() int
}

type Rotable struct {
	alpha           angle.Angle
	angularVelocity int
}

func (r *Rotable) GetAngle() int {
	return r.alpha.Value
}

func (r *Rotable) SetAngle(newValue int) error {
	r.alpha.Value = newValue
	return nil
}

func (r *Rotable) GetDivision() int {
	return r.alpha.Division
}

func (r *Rotable) GetAngularVelocity() int {
	return r.angularVelocity
}

type Rotate struct {
	Rotable IRotable
}

func (r *Rotate) Execute() {
	newValue := (r.Rotable.GetAngle() + r.Rotable.GetAngularVelocity()) % r.Rotable.GetDivision()
	if err := r.Rotable.SetAngle(newValue); err != nil {
		panic(err)
	}
}
