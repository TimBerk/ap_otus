package moving

import "additional/internal/models/vector"

type IMovable interface {
	GetVelocity() vector.Vector
	GetPosition() vector.Vector
	SetPosition(newVector vector.Vector) error
}

type Movable struct {
	velocity vector.Vector
	position vector.Vector
}

func (m *Movable) GetVelocity() vector.Vector {
	return m.velocity
}

func (m *Movable) GetPosition() vector.Vector {
	return m.position
}

func (m *Movable) SetPosition(newVector vector.Vector) error {
	m.position = newVector
	return nil
}

type Move struct {
	movable IMovable
}

func (m *Move) Execute() {
	newPosition := vector.Plus(m.movable.GetPosition(), m.movable.GetVelocity())
	if err := m.movable.SetPosition(newPosition); err != nil {
		panic(err)
	}
}
