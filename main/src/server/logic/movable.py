import zope

from server.interfaces.movable import IMovable
from server.models import Vector


@zope.interface.implementer(IMovable)
class Move:
    """Движение объекта"""

    def __init__(self, object):
        self.object = object

    def get_position(self) -> Vector:
        return self.object.position

    def set_position(self, value: Vector) -> None:
        self.object.position = value

    def get_velocity(self) -> Vector:
        return self.object.velocity

    def set_velocity(self, value: Vector) -> None:
        self.object.velocity = value
