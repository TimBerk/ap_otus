import zope

from server.errors import MoveParamException
from server.interfaces.cmd import ICommand
from server.models import Vector


@zope.interface.implementer(ICommand)
class MoveCommand:
    """Команда движения объекта"""

    def __init__(self, object):
        self.object = object

    def execute(self) -> None:
        """Установка новой позиции"""

        position = self.object.get_position()
        if not isinstance(position, Vector):
            raise MoveParamException('Incorrect position value')

        velocity = self.object.get_velocity()
        if not isinstance(velocity, Vector):
            raise MoveParamException('Incorrect velocity value')

        self.object.set_position(position + velocity)
