package cmd

import (
	"container/list"
	"errors"
	"fmt"
)

var ErrRepeat = errors.New("the command could not repeat")

type ICommand interface {
	Execute() error
}

type ICommandQueue interface {
	Add(command ICommand)
	Get() (ICommand, error)
}

type CommandQueue[T ICommand] struct {
	Queue *list.List
}

func NewCommandQueue() *CommandQueue[ICommand] {
	return &CommandQueue[ICommand]{
		Queue: list.New(),
	}
}

func (c CommandQueue[ICommand]) Add(command ICommand) {
	c.Queue.PushBack(command)
}

func (c CommandQueue[ICommand]) Get() (ICommand, error) {
	if c.Queue.Len() < 1 {
		var zero ICommand
		return zero, fmt.Errorf("queue is empty")
	}

	command := c.Queue.Front()
	value := command.Value.(ICommand)
	c.Queue.Remove(command)

	return value, nil
}
