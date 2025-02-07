package integration

import (
	"additional/internal/services/cmd"
	"additional/internal/services/cmd/log"
	"additional/internal/services/cmd/repeat"
	"bytes"
	"errors"
	"testing"

	"github.com/sirupsen/logrus"
	"github.com/stretchr/testify/assert"
)

type TestErrorCommand struct{}

func (tec TestErrorCommand) Execute() error {
	return errors.New("test Error Command")
}

func TestCommandQueue(t *testing.T) {
	var counter int
	var buf bytes.Buffer
	logrus.SetOutput(&buf)
	logrus.SetFormatter(&logrus.TextFormatter{
		DisableTimestamp: true,
	})
	logrus.SetLevel(logrus.WarnLevel)
	expectedLog := "level=warning msg=\"the command could not repeat: test Error Command\" command=log\n"

	maxRetries := 1
	queue := cmd.NewCommandQueue()
	queue.Add(TestErrorCommand{})

	for queue.Queue.Len() > 0 {
		currentCommand, _ := queue.Get()

		err := currentCommand.Execute()
		if err != nil {
			if errors.Is(err, cmd.ErrRepeat) {
				log.HandlerLog(err, queue)
			} else {
				repeat.HandlerRepeat(currentCommand, maxRetries, queue)
			}
		}

		counter++
	}
	logs := buf.String()

	assert.Equal(t, 4, counter)
	if logs != expectedLog {
		t.Errorf("Expected log:\n%q\nGot:\n%q", expectedLog, logs)
	}
}
