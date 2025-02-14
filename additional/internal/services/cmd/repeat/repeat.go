// Пакет отвечает за реализацию команды-повтора выполнения другой команды.
package repeat

import (
	"additional/internal/services/cmd"
	"fmt"
	"reflect"
)

type Repeat struct {
	command    cmd.ICommand
	retries    int
	maxRetries int
}

func NewRepeat(command cmd.ICommand, maxRetries int) *Repeat {
	return &Repeat{
		command:    command,
		maxRetries: maxRetries,
	}
}

func (cr *Repeat) Execute() error {
	err := cr.command.Execute()
	if cr.retries < cr.maxRetries {
		cr.retries++
		return err
	}
	return fmt.Errorf("%w: %v", cmd.ErrRepeat, err)
}

func HandlerRepeat(command cmd.ICommand, maxRetries int, queue *cmd.CommandQueue[cmd.ICommand]) {
	commandType := reflect.TypeOf(command)
	if commandType != reflect.TypeOf((*Repeat)(nil)).Elem() {
		command = NewRepeat(command, maxRetries)
	}
	queue.Add(command)
}
