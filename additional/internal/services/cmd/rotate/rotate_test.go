package rotate

import (
	"additional/internal/models/angle"
	"additional/internal/services/rotating"
	"errors"
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/mock"
)

type MockRotable struct {
	mock.Mock
}

func (m *MockRotable) GetAngle() (int, error) {
	args := m.Called()
	return args.Get(0).(int), nil
}

func (m *MockRotable) SetAngle(newAngle int) error {
	args := m.Called(newAngle)
	return args.Error(0)
}

func (m *MockRotable) GetDivision() (int, error) {
	args := m.Called()
	return args.Get(0).(int), nil
}

func (m *MockRotable) GetAngularVelocity() (int, error) {
	args := m.Called()
	return args.Get(0).(int), nil
}

func TestRotate(t *testing.T) {
	rotable := rotating.NewRotatable(angle.Angle{Value: 0, Division: 10}, 10)
	rotate := NewRotate(rotable)

	err := rotate.Execute()

	assert.Nil(t, err)
	newAngle, err := rotable.GetAngle()
	assert.Nil(t, err)
	assert.Equal(t, 0, newAngle, "Ожидаемый угол: (0, 10)")
}

func TestRotateInvalidAngleChange(t *testing.T) {
	mockRotable := new(MockRotable)
	mockRotable.On("GetAngle").Return(1, nil)
	mockRotable.On("GetAngularVelocity").Return(10, nil)
	mockRotable.On("GetDivision").Return(20, nil)
	mockRotable.On("SetAngle", mock.Anything).Return(errors.New("Ошибка изменения положения"))
	rotate := NewRotate(mockRotable)

	err := rotate.Execute()

	assert.Error(t, err, "Ожидалась паника при невозможности изменить угол")
	mockRotable.AssertExpectations(t)
}
