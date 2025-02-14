// Пакет для обработки команды движения по прямой
package move

import (
	"additional/internal/models/vector"
	"additional/internal/services/moving"
)

type Move struct {
	object moving.IMovable
}

func NewMove(object moving.IMovable) *Move {
	return &Move{object: object}
}

func (m *Move) Execute() error {
	position, err := m.object.GetPosition()
	if err != nil {
		return err
	}

	velocity, err := m.object.GetVelocity()
	if err != nil {
		return err
	}

	newPosition := vector.Plus(position, velocity)
	return m.object.SetPosition(newPosition)
}
