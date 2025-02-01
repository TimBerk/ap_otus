package moving

import (
	"additional/internal/models/vector"
	"errors"
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/mock"
)

type MockMovable struct {
	mock.Mock
}

func (m *MockMovable) GetVelocity() vector.Vector {
	args := m.Called()
	return args.Get(0).(vector.Vector)
}

func (m *MockMovable) GetPosition() vector.Vector {
	args := m.Called()
	return args.Get(0).(vector.Vector)
}

func (m *MockMovable) SetPosition(newPosition vector.Vector) error {
	args := m.Called(newPosition)
	return args.Error(0)
}

func TestMove(t *testing.T) {
	movable := &Movable{
		position: vector.Vector{X: 12, Y: 5},
		velocity: vector.Vector{X: -7, Y: 3},
	}
	move := Move{movable: movable}
	move.Execute()

	newPosition := movable.GetPosition()
	assert.Equal(t, vector.Vector{X: 5, Y: 8}, newPosition, "Ожидаемое положение после движения: (5, 8)")
}

func TestMoveNilMovable(t *testing.T) {
	move := Move{movable: nil}
	assert.Panics(t, func() { move.Execute() }, "Ожидалась паника при попытке сдвинуть nil объект")
}

func TestMoveInvalidPosition(t *testing.T) {
	mockMovable := new(MockMovable)
	mockMovable.On("GetPosition").Return(vector.Vector{}, errors.New("ошибка чтения положения"))

	move := Move{movable: mockMovable}
	assert.Panics(t, func() { move.Execute() }, "Ожидалась паника при невозможности прочитать положение")

	mockMovable.AssertExpectations(t)
}

func TestMoveInvalidVelocity(t *testing.T) {
	mockMovable := new(MockMovable)
	mockMovable.On("GetPosition").Return(vector.Vector{X: 12, Y: 5}, nil)
	mockMovable.On("GetVelocity").Return(vector.Vector{}, errors.New("ошибка чтения скорости"))

	move := Move{movable: mockMovable}
	assert.Panics(t, func() { move.Execute() }, "Ожидалась паника при невозможности прочитать скорость")

	mockMovable.AssertExpectations(t)
}

func TestMoveInvalidPositionChange(t *testing.T) {
	mockMovable := new(MockMovable)
	mockMovable.On("GetPosition").Return(vector.Vector{X: 12, Y: 5}, nil)
	mockMovable.On("GetVelocity").Return(vector.Vector{X: -7, Y: 3}, nil)
	mockMovable.On("SetPosition", mock.Anything).Return(errors.New("ошибка изменения положения"))

	move := Move{movable: mockMovable}
	assert.Panics(t, func() { move.Execute() }, "Ожидалась паника при невозможности изменить положение")

	mockMovable.AssertExpectations(t)
}
