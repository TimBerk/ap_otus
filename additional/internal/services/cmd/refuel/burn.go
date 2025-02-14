// Пакет для обработки команды сжигания топлива
package refuel

import (
	"additional/internal/services/cmd"
	base_refuel "additional/internal/services/refueling"
)

type BurnFuelCommand struct {
	object base_refuel.IRefuel
}

func NewBurnFuelCommand(object base_refuel.IRefuel) *BurnFuelCommand {
	return &BurnFuelCommand{object: object}
}

func (bfc BurnFuelCommand) Execute() error {
	fuel, err := bfc.object.GetFuel()
	if err != nil {
		return err
	}

	rateOfFule, err := bfc.object.GetRateOfFlow()
	if err != nil {
		return err
	}

	newFuel := fuel - rateOfFule
	if newFuel < 0 {
		return cmd.ErrCommandException
	}
	return bfc.object.SetFuel(newFuel)
}
