package integration

import (
	"additional/internal/models/angle"
	"additional/internal/models/vector"
	"additional/internal/objects/spaceship"
	"additional/internal/services/cmd/change_velocity"
	"math"
	"testing"
)

func TestChangeVelocity_Execute(t *testing.T) {
	tests := []struct {
		name        string
		initialVel  vector.Vector
		angle       float64
		expectedVel vector.Vector
		expectError bool
	}{
		{
			name:        "Поворот на 90 градусов",
			initialVel:  vector.Vector{X: 10, Y: 0},
			angle:       math.Pi / 2,
			expectedVel: vector.Vector{X: 0, Y: 10},
			expectError: false,
		},
		{
			name:        "Поворот на 180 градусов",
			initialVel:  vector.Vector{X: 10, Y: 0},
			angle:       math.Pi,
			expectedVel: vector.Vector{X: -10, Y: 0},
			expectError: false,
		},
		{
			name:        "Поворот на 45 градусов",
			initialVel:  vector.Vector{X: 10, Y: 0},
			angle:       math.Pi / 4,
			expectedVel: vector.Vector{X: 7, Y: 7},
			expectError: false,
		},
		{
			name:        "Неподвижный объект",
			initialVel:  vector.Vector{X: 0, Y: 0},
			angle:       math.Pi / 2,
			expectedVel: vector.Vector{X: 0, Y: 0},
			expectError: false,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			obj := spaceship.NewSpaceship(angle.Angle{Value: 0, Division: 10}, 10, 10, 1, tt.initialVel, vector.Vector{X: 0, Y: 0})
			cv := change_velocity.NewChagneVelocity(obj, tt.angle)

			err := cv.Execute()
			if (err != nil) != tt.expectError {
				t.Errorf("Ожидалась ошибка: %v, получено: %v", tt.expectError, err)
			}

			newVel, _ := obj.GetVelocity()
			if newVel != tt.expectedVel {
				t.Errorf("Ожидаемая скорость: %v, получено: %v", tt.expectedVel, newVel)
			}
		})
	}
}
