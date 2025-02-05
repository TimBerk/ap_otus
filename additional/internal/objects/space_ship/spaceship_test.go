package spaceship

import (
	"additional/internal/models/angle"
	"additional/internal/services/rotating"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestRotate(t *testing.T) {
	spaceship := &Spaceship{
		alpha:           angle.Angle{Value: 0, Division: 10},
		angularVelocity: 10,
	}

	rotate := rotating.Rotate{Rotable: spaceship}
	rotate.Execute()

	newAngle := spaceship.GetAngle()
	assert.Equal(t, 0, newAngle, "Ожидаемый угол: (0, 10)")
}
