package vector

type Vector struct {
	X, Y int
}

func Plus(base, other Vector) Vector {
	return Vector{
		X: base.X + other.X,
		Y: base.Y + other.Y,
	}
}
