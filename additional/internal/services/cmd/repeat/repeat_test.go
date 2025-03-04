package repeat

import (
	"additional/internal/services/cmd"
	"bytes"
	"fmt"
	"testing"

	"github.com/stretchr/testify/assert"
)

type SimpleCommand struct{}

func (sc SimpleCommand) Execute() error {
	fmt.Print("Test execute command")
	return nil
}

func TestRepeat(t *testing.T) {
	var buf bytes.Buffer
	expectedOutput := "Test execute command"
	baseCommand := &SimpleCommand{}
	repeatCommand := NewRepeat(baseCommand, 1)

	err := repeatCommand.Execute()

	assert.Nil(t, err)
	fmt.Fprint(&buf, expectedOutput)
	actualOutput := buf.String()
	if actualOutput != expectedOutput {
		t.Errorf("Expected output '%s' does not match actual output '%s'", expectedOutput, actualOutput)
	}
}

func TestHandlerRepeat(t *testing.T) {
	queue := cmd.NewCommandQueue()
	baseCommand := &SimpleCommand{}

	HandlerRepeat(baseCommand, 1, queue)

	assert.Equal(t, 1, queue.Queue.Len())
}
