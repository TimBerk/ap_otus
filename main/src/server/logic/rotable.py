import zope

from server.errors import RotateParamException
from server.interfaces.rotable import IRotable
from server.models import Angle


@zope.interface.implementer(IRotable)
class Rotate:
    """Поворот объекта"""

    def __init__(self, rotable):
        self.rotable = rotable

    def get_angle(self) -> int:
        return self.rotable.alpha.value

    def set_angel(self, new_value: Angle):
        self.rotable.alpha = new_value

    def get_division(self) -> int:
        return self.rotable.alpha.division

    def get_angular_velocity(self) -> int:
        return self.rotable.angular_velocity

    def execute(self) -> None:
        """Установка нового угла при повороте"""

        if not isinstance(self.rotable.alpha, Angle):
            raise RotateParamException('Incorrect alpha value')

        if not isinstance(self.rotable.angular_velocity, int):
            raise RotateParamException('Incorrect angular velocity value')

        new_angle = (self.get_angle() + self.get_angular_velocity()) % self.get_division()
        self.set_angel(Angle(new_angle, self.get_division()))
