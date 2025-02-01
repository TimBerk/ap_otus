import dataclasses


@dataclasses.dataclass
class Vector:
    x: int
    y: int

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


@dataclasses.dataclass
class Angle:
    value: int
    division: int
