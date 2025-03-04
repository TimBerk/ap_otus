// Пакет отвечает за реализацию команды-повтора выполнения другой команды.
package repeat

import (
	"additional/internal/services/cmd"
	"fmt"
	"reflect"
)

type CommandRepeat struct {
	command    cmd.ICommand
	retries    int
	maxRetries int
}

func NewCommandRepeat(command cmd.ICommand, maxRetries int) *CommandRepeat {
	return &CommandRepeat{
		command:    command,
		maxRetries: maxRetries,
	}
}

func (cr *CommandRepeat) Execute() error {
	err := cr.command.Execute()
	if cr.retries < cr.maxRetries {
		cr.retries++
		return err
	}
	return fmt.Errorf("%w: %v", cmd.ErrRepeat, err)
}

func HandlerRepeat(command cmd.ICommand, maxRetries int, queue *cmd.CommandQueue[cmd.ICommand]) {
	commandType := reflect.TypeOf(command)
	if commandType != reflect.TypeOf((*CommandRepeat)(nil)).Elem() {
		command = NewCommandRepeat(command, maxRetries)
	}
	queue.Add(command)
}
