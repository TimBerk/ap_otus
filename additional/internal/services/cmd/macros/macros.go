// Пакет для обработки макрокоманды
package macros

import (
	"additional/internal/services/cmd"
)

type Macros struct {
	queue cmd.CommandQueue[cmd.ICommand]
}

func NewMacros(queue cmd.CommandQueue[cmd.ICommand]) *Macros {
	return &Macros{queue: queue}
}

func (m *Macros) Execute() error {
	for m.queue.Queue.Len() > 0 {
		currentCommand, _ := m.queue.Get()
		err := currentCommand.Execute()
		if err != nil {
			return cmd.ErrCommandException
		}
	}
	return nil
}
