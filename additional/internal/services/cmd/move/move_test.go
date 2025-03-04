package move

import (
	"additional/internal/models/vector"
	"additional/internal/services/moving"
	"errors"
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/mock"
)

type MockMovable struct {
	mock.Mock
}

func (m *MockMovable) GetVelocity() (vector.Vector, error) {
	args := m.Called()
	return args.Get(0).(vector.Vector), args.Error(1)
}

func (m *MockMovable) GetPosition() (vector.Vector, error) {
	args := m.Called()
	return args.Get(0).(vector.Vector), args.Error(1)
}

func (m *MockMovable) SetPosition(newPosition vector.Vector) error {
	args := m.Called(newPosition)
	return args.Error(0)
}

func TestMove(t *testing.T) {
	movable := moving.NewMovable(vector.Vector{X: 12, Y: 5}, vector.Vector{X: -7, Y: 3})
	move := NewMove(movable)

	err := move.Execute()

	assert.Nil(t, err)
	newPosition, _ := movable.GetPosition()
	assert.Equal(t, vector.Vector{X: 5, Y: 8}, newPosition, "Ожидаемое положение после движения: (5, 8)")
}

func TestMoveInvalidPosition(t *testing.T) {
	mockMovable := new(MockMovable)
	mockMovable.On("GetPosition").Return(vector.Vector{}, errors.New("ошибка чтения положения"))
	move := NewMove(mockMovable)

	err := move.Execute()

	assert.Error(t, err)
	mockMovable.AssertExpectations(t)
}

func TestMoveInvalidVelocity(t *testing.T) {
	mockMovable := new(MockMovable)
	mockMovable.On("GetPosition").Return(vector.Vector{X: 12, Y: 5}, nil)
	mockMovable.On("GetVelocity").Return(vector.Vector{}, errors.New("ошибка чтения скорости"))
	move := NewMove(mockMovable)

	err := move.Execute()

	assert.Error(t, err)
	mockMovable.AssertExpectations(t)
}

func TestMoveInvalidPositionChange(t *testing.T) {
	mockMovable := new(MockMovable)
	mockMovable.On("GetPosition").Return(vector.Vector{X: 12, Y: 5}, nil)
	mockMovable.On("GetVelocity").Return(vector.Vector{X: -7, Y: 3}, nil)
	mockMovable.On("SetPosition", mock.Anything).Return(errors.New("ошибка изменения положения"))
	move := NewMove(mockMovable)

	err := move.Execute()

	assert.Error(t, err, "Ожидалась паника при невозможности изменить положение")
	mockMovable.AssertExpectations(t)
}
