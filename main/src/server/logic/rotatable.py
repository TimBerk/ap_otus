import zope

from server.interfaces.rotatable import IRotatable
from server.models import Angle


@zope.interface.implementer(IRotatable)
class Rotate:
    """Поворот объекта"""

    def __init__(self, object):
        self.object = object

    def get_angle(self) -> Angle:
        return self.object.alpha

    def set_angle(self, new_value: Angle):
        self.object.alpha = new_value

    def get_division(self) -> int:
        return self.object.alpha.division

    def get_angular_velocity(self) -> int:
        return self.object.angular_velocity
