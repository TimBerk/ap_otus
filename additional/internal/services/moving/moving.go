package moving

import "additional/internal/models/vector"

type IMovable interface {
	GetVelocity() (vector.Vector, error)
	GetPosition() (vector.Vector, error)
	SetPosition(newVector vector.Vector) error
}

type Movable struct {
	velocity vector.Vector
	position vector.Vector
}

func NewMovable(velocity vector.Vector, position vector.Vector) *Movable {
	return &Movable{velocity: velocity, position: position}
}

func (m *Movable) GetVelocity() (vector.Vector, error) {
	return m.velocity, nil
}

func (m *Movable) GetPosition() (vector.Vector, error) {
	return m.position, nil
}

func (m *Movable) SetPosition(newVector vector.Vector) error {
	m.position = newVector
	return nil
}
