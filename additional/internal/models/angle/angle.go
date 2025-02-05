package angle

type Angle struct {
	Value    int
	Division int
}

func NewAngle(value int, division int) *Angle {
	if value >= division {
		panic("Incorrect value, it must less then division")
	}

	return &Angle{
		Value:    value,
		Division: division,
	}
}
