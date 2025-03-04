package spaceship

import (
	"additional/internal/models/angle"
	"additional/internal/services/cmd/rotate"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestRotate(t *testing.T) {
	spaceship := &Spaceship{
		alpha:           angle.Angle{Value: 0, Division: 10},
		angularVelocity: 10,
	}

	rotateCmd := rotate.NewRotate(spaceship)
	err := rotateCmd.Execute()

	assert.Nil(t, err)
	newAngle, err := spaceship.GetAngle()
	assert.Nil(t, err)
	assert.Equal(t, 0, newAngle, "Ожидаемый угол: (0, 10)")
}
