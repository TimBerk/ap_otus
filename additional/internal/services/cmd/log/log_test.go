package log

import (
	"bytes"
	"errors"
	"testing"

	"additional/internal/services/cmd"

	"github.com/sirupsen/logrus"
	"github.com/stretchr/testify/assert"
)

func TestCommandLog(t *testing.T) {
	var buf bytes.Buffer
	logrus.SetOutput(&buf)
	logrus.SetFormatter(&logrus.TextFormatter{
		DisableTimestamp: true,
	})
	logrus.SetLevel(logrus.WarnLevel)
	expectedLog := "level=warning msg=\"test error\" command=log\n"
	command := NewLog(errors.New("test error"))

	err := command.Execute()
	logs := buf.String()

	assert.Nil(t, err)
	if logs != expectedLog {
		t.Errorf("Expected log:\n%q\nGot:\n%q", expectedLog, logs)
	}
}

func TestHandlerLog(t *testing.T) {
	queue := cmd.NewCommandQueue()

	HandlerLog(errors.New("test error"), queue)

	assert.Equal(t, 1, queue.Queue.Len())
}
