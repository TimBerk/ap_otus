import zope

from server.errors import MoveParamException
from server.interfaces.cmd import ICommand
from server.interfaces.movable import IMovable
from server.models import Vector


@zope.interface.implementer(IMovable, ICommand)
class Move:
    """Движение объекта"""

    def __init__(self, movable):
        self.movable = movable

    def get_position(self) -> Vector:
        return self.movable.position

    def get_velocity(self) -> Vector:
        return self.movable.velocity

    def set_position(self, new_position: Vector) -> None:
        self.movable.position = new_position

    def execute(self) -> None:
        """Установка новой позиции"""

        if not isinstance(self.movable.position, Vector):
            raise MoveParamException('Incorrect position value')

        if not isinstance(self.movable.velocity, Vector):
            raise MoveParamException('Incorrect velocity value')

        self.set_position(self.get_position() + self.get_velocity())
