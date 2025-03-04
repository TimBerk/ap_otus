package macros

import (
	"additional/internal/models/angle"
	"additional/internal/models/vector"
	"additional/internal/objects/spaceship"
	"additional/internal/services/cmd"
	"additional/internal/services/cmd/move"
	"additional/internal/services/cmd/refuel"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestSuccessMacros(t *testing.T) {
	object := spaceship.NewSpaceship(angle.Angle{Value: 0, Division: 10}, 10, 10, 1, vector.Vector{X: 0, Y: 0}, vector.Vector{X: 0, Y: 0})
	queue := cmd.NewCommandQueue()
	queue.Add(refuel.NewCheckFuelCommand(object))
	queue.Add(move.NewMove(object))
	queue.Add(refuel.NewBurnFuelCommand(object))
	currentCommand := NewMacros(*queue)

	err := currentCommand.Execute()

	assert.Nil(t, err)
}

func TestErrorMacros(t *testing.T) {
	object := spaceship.NewSpaceship(angle.Angle{Value: 0, Division: 10}, 10, 0, 1, vector.Vector{X: 0, Y: 0}, vector.Vector{X: 0, Y: 0})
	queue := cmd.NewCommandQueue()
	queue.Add(refuel.NewCheckFuelCommand(object))
	queue.Add(move.NewMove(object))
	queue.Add(refuel.NewBurnFuelCommand(object))
	currentCommand := NewMacros(*queue)

	err := currentCommand.Execute()

	if err != cmd.ErrCommandException {
		t.Errorf("macros error = %v, expectedErr %v", err, cmd.ErrCommandException)
	}

}
