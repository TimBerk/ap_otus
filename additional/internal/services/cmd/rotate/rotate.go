// Пакет для обработки команды поворота
package rotate

import (
	"additional/internal/services/rotating"
)

type Rotate struct {
	object rotating.IRotable
}

func NewRotate(object rotating.IRotable) *Rotate {
	return &Rotate{object: object}
}

func (r *Rotate) Execute() error {
	angle, err := r.object.GetAngle()
	if err != nil {
		return err
	}

	angularVelocity, err := r.object.GetAngularVelocity()
	if err != nil {
		return err
	}

	division, err := r.object.GetDivision()
	if err != nil {
		return err
	}

	newValue := (angle + angularVelocity) % division
	return r.object.SetAngle(newValue)
}
