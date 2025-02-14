import zope

from server.errors import RotateParamException
from server.interfaces.cmd import ICommand
from server.models import Angle


@zope.interface.implementer(ICommand)
class RotateCommand:
    """Команда поворота объекта"""

    def __init__(self, object):
        self.object = object

    def execute(self) -> None:
        """Установка нового угла при повороте"""

        alpha = self.object.get_angle()
        if not isinstance(alpha, Angle):
            raise RotateParamException('Incorrect alpha value')

        angular_velocity = self.object.get_angular_velocity()
        if not isinstance(angular_velocity, int):
            raise RotateParamException('Incorrect angular velocity value')

        division = self.object.get_division()
        new_angle = (alpha.value + angular_velocity) % division
        self.object.set_angle(Angle(new_angle, division))
