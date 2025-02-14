// Пакет отвечает за реализацию команды-логера исключений.
package log

import (
	"additional/internal/services/cmd"

	"github.com/sirupsen/logrus"
)

type CommandLog struct {
	Exception error
}

func NewCommandLog(exception error) *CommandLog {
	return &CommandLog{
		Exception: exception,
	}
}

func (cl CommandLog) Execute() error {
	logrus.WithFields(logrus.Fields{"command": "log"}).Warn(cl.Exception)
	return nil
}

func HandlerLog(exception error, queue *cmd.CommandQueue[cmd.ICommand]) {
	newCommand := NewCommandLog(exception)
	queue.Add(newCommand)
}
