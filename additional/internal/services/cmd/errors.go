package cmd

import "errors"

var ErrCommandException = errors.New("the command queue could not continue work")
