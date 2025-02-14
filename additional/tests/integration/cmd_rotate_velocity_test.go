package integration

import (
	"additional/internal/models/angle"
	"additional/internal/models/vector"
	"additional/internal/objects/spaceship"
	"additional/internal/services/cmd/rotate_velocity"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestRotateVelocity_Execute(t *testing.T) {
	tests := []struct {
		name             string
		initialAngle     angle.Angle
		angularVelocity  int
		initialVelocity  vector.Vector
		expectedVelocity vector.Vector
		expectedAngle    int
		expectError      bool
		expectedError    error
	}{
		{
			name:             "Поворот на 90 градусов",
			initialAngle:     angle.Angle{Value: 0, Division: 360},
			angularVelocity:  90,
			initialVelocity:  vector.Vector{X: 10, Y: 0},
			expectedVelocity: vector.Vector{X: -4, Y: 9},
			expectedAngle:    90,
			expectError:      false,
			expectedError:    nil,
		},
		{
			name:             "Поворот на 180 градусов",
			initialAngle:     angle.Angle{Value: 0, Division: 360},
			angularVelocity:  180,
			initialVelocity:  vector.Vector{X: 10, Y: 0},
			expectedVelocity: vector.Vector{X: -6, Y: -8},
			expectedAngle:    180,
			expectError:      false,
			expectedError:    nil,
		},
		{
			name:             "Неподвижный объект",
			initialAngle:     angle.Angle{Value: 0, Division: 360},
			angularVelocity:  90,
			initialVelocity:  vector.Vector{X: 0, Y: 0},
			expectedVelocity: vector.Vector{X: 0, Y: 0},
			expectedAngle:    90,
			expectError:      false,
			expectedError:    nil,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			obj := spaceship.NewSpaceship(tt.initialAngle, tt.angularVelocity, 10, 1, tt.initialVelocity, vector.Vector{X: 0, Y: 0})
			rotateVelCmd := rotate_velocity.NewRotateVelocity(obj)

			err := rotateVelCmd.Execute()
			assert.Nil(t, err)

			newVelocity, err := obj.GetVelocity()
			assert.Nil(t, err)
			if newVelocity != tt.expectedVelocity {
				t.Errorf("Ожидаемая скорость: %v, получено: %v", tt.expectedVelocity, newVelocity)
			}

			newAngle, err := obj.GetAngle()
			assert.Nil(t, err)
			if newAngle != tt.expectedAngle {
				t.Errorf("Ожидаемый угол: %v, получено: %v", tt.expectedAngle, newAngle)
			}
		})
	}
}
