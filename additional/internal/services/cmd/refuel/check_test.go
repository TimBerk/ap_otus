package refuel

import (
	"additional/internal/models/angle"
	"additional/internal/models/vector"
	"additional/internal/objects/spaceship"
	"additional/internal/services/cmd"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCheck(t *testing.T) {
	object := spaceship.NewSpaceship(angle.Angle{Value: 0, Division: 10}, 10, 10, 1, vector.Vector{X: 0, Y: 0}, vector.Vector{X: 0, Y: 0})
	command := NewCheckFuelCommand(object)

	err := command.Execute()

	assert.Nil(t, err)
}

func TestCheckInvalidResult(t *testing.T) {
	object := spaceship.NewSpaceship(angle.Angle{Value: 0, Division: 10}, 10, 0, 1, vector.Vector{X: 0, Y: 0}, vector.Vector{X: 0, Y: 0})
	command := NewCheckFuelCommand(object)

	err := command.Execute()

	if err != cmd.ErrCommandException {
		t.Errorf("Execute() error = %v, expectedErr %v", err, cmd.ErrCommandException)
	}
}
