package rotating

import (
	"additional/internal/models/angle"
	"errors"
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/mock"
)

type MockRotable struct {
	mock.Mock
}

func (m *MockRotable) GetAngle() int {
	args := m.Called()
	return args.Get(0).(int)
}

func (m *MockRotable) SetAngle(newAngle int) error {
	args := m.Called(newAngle)
	return args.Error(0)
}

func (m *MockRotable) GetDivision() int {
	args := m.Called()
	return args.Get(0).(int)
}

func (m *MockRotable) GetAngularVelocity() int {
	args := m.Called()
	return args.Get(0).(int)
}

func TestRotate(t *testing.T) {
	rotable := &Rotable{
		alpha:           angle.Angle{Value: 0, Division: 10},
		angularVelocity: 10,
	}
	rotate := Rotate{Rotable: rotable}
	rotate.Execute()

	newAngle := rotable.GetAngle()
	assert.Equal(t, 0, newAngle, "Ожидаемый угол: (0, 10)")
}

func TestRotateInvalidAngleChange(t *testing.T) {
	mockRotable := new(MockRotable)
	mockRotable.On("GetAngle").Return(1, nil)
	mockRotable.On("GetAngularVelocity").Return(10, nil)
	mockRotable.On("GetDivision").Return(20, nil)
	mockRotable.On("SetAngle", mock.Anything).Return(errors.New("Ошибка изменения положения"))

	rotate := Rotate{Rotable: mockRotable}
	assert.Panics(t, func() { rotate.Execute() }, "Ожидалась паника при невозможности изменить угол")

	mockRotable.AssertExpectations(t)
}
