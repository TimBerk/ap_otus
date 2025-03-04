// Пакет для обработки макрокоманды длительного движения по прямой
package forwardmotion

import (
	"additional/internal/services/cmd"
	"additional/internal/services/cmd/macros"
)

type ForwardMotion struct {
	macros macros.Macros
}

func NewForwardMotion(check cmd.ICommand, move cmd.ICommand, refuel cmd.ICommand) *ForwardMotion {
	queue := cmd.NewCommandQueue()
	queue.Add(check)
	queue.Add(move)
	queue.Add(refuel)
	macros := macros.NewMacros(*queue)
	return &ForwardMotion{macros: *macros}
}

func (m *ForwardMotion) Execute() error {
	return m.macros.Execute()
}
