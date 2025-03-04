// Пакет для обработки команды модификации вектора мгновенной скорости при повороте
package rotate_velocity

import (
	"additional/internal/services/cmd/change_velocity"
	"additional/internal/services/cmd/rotate"
)

type RotateVelocity struct {
	object change_velocity.IChangeVelocity
}

func NewRotateVelocity(object change_velocity.IChangeVelocity) *RotateVelocity {
	return &RotateVelocity{object: object}
}

func (rv *RotateVelocity) Execute() error {
	cmdRotate := rotate.NewRotate(rv.object)
	err := cmdRotate.Execute()
	if err != nil {
		return err
	}

	angle, err := rv.object.GetAngle()
	if err != nil {
		return err
	}

	cmdChangeVelocity := change_velocity.NewChagneVelocity(rv.object, float64(angle))
	return cmdChangeVelocity.Execute()
}
