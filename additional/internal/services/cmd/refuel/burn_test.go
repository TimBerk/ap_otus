package refuel

import (
	"additional/internal/models/angle"
	"additional/internal/models/vector"
	"additional/internal/objects/spaceship"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestBurn(t *testing.T) {
	object := spaceship.NewSpaceship(angle.Angle{Value: 0, Division: 10}, 10, 10, 1, vector.Vector{X: 0, Y: 0}, vector.Vector{X: 0, Y: 0})
	command := NewBurnFuelCommand(object)

	err := command.Execute()

	assert.Nil(t, err)
	newFuel, err := object.GetFuel()
	assert.Nil(t, err)
	assert.Equal(t, 9, newFuel, "Ожидаемый уровень топлива: 9")
}
