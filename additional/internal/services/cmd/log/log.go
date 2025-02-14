// Пакет отвечает за реализацию команды-логера исключений.
package log

import (
	"additional/internal/services/cmd"

	"github.com/sirupsen/logrus"
)

type Log struct {
	Exception error
}

func NewLog(exception error) *Log {
	return &Log{
		Exception: exception,
	}
}

func (cl Log) Execute() error {
	logrus.WithFields(logrus.Fields{"command": "log"}).Warn(cl.Exception)
	return nil
}

func HandlerLog(exception error, queue *cmd.CommandQueue[cmd.ICommand]) {
	newCommand := NewLog(exception)
	queue.Add(newCommand)
}
