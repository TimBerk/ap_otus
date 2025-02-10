// Пакет для обработки команды модификации вектора мгновенной скорости при повороте
package change_velocity

import (
	"additional/internal/models/vector"
	"fmt"
	"math"
)

type IChangeVelocity interface {
	GetVelocity() (vector.Vector, error)
	SetVelocity(value vector.Vector) error

	GetAngle() (int, error)
	SetAngle(value int) error
	GetDivision() (int, error)
	GetAngularVelocity() (int, error)
}

type ChangeVelocity struct {
	object IChangeVelocity
	angle  float64
}

func NewChagneVelocity(object IChangeVelocity, angle float64) *ChangeVelocity {
	return &ChangeVelocity{object: object, angle: angle}
}

func (cv *ChangeVelocity) Execute() error {
	velocity, err := cv.object.GetVelocity()
	if err != nil {
		return fmt.Errorf("ошибка при получении скорости: %v", err)
	}

	if velocity.X == 0 && velocity.Y == 0 {
		return nil
	}

	vx := float64(velocity.X)
	vy := float64(velocity.Y)

	speed := math.Hypot(vx, vy)
	newAngle := math.Atan2(vy, vx) + cv.angle

	newX := int(math.Round(speed * math.Cos(newAngle)))
	newY := int(math.Round(speed * math.Sin(newAngle)))

	return cv.object.SetVelocity(vector.Vector{X: newX, Y: newY})
}
