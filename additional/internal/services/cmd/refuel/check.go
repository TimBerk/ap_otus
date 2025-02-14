// Пакет для обработки команды проверки топлива
package refuel

import (
	"additional/internal/services/cmd"
	base_refuel "additional/internal/services/refueling"
)

type CheckFuelCommand struct {
	object base_refuel.IRefuel
}

func NewCheckFuelCommand(object base_refuel.IRefuel) *CheckFuelCommand {
	return &CheckFuelCommand{object: object}
}

func (cfc CheckFuelCommand) Execute() error {
	if cfc.object.CheckFuel() {
		return nil
	}

	return cmd.ErrCommandException
}
