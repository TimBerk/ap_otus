import math

import zope

from server.cmd.rotate import RotateCommand
from server.errors import ChangeVelocityCommandException
from server.interfaces.cmd import ICommand
from server.models import Vector
from server.types import MovableRotatable


@zope.interface.implementer(ICommand)
class ChangeVelocityCommand:
    """Команда изменения вектора мгновенной скорости"""

    def __init__(self, object: MovableRotatable, angle: float):
        self.object = object
        self.angle = angle

    def execute(self) -> None:
        """Установка вектора мгновенной скорости"""

        velocity = self.object.get_velocity()
        if not isinstance(velocity, Vector):
            raise ChangeVelocityCommandException()

        if velocity.x == 0 and velocity.y == 0:
            return

        vx = float(velocity.x)
        vy = float(velocity.y)

        speed = math.hypot(vx, vy)
        new_angle = math.atan2(vy, vx) + self.angle

        new_x = int(round(speed * math.cos(new_angle)))
        new_y = int(round(speed * math.sin(new_angle)))

        return self.object.set_velocity(Vector(new_x, new_y))


@zope.interface.implementer(ICommand)
class RotateVelocityCommand:
    """Команда изменения вектора мгновенной скорости при повороте"""

    def __init__(self, object: MovableRotatable):
        self.object = object

    def execute(self) -> None:
        """Установка вектора мгновенной скорости"""

        rotate = RotateCommand(self.object)
        rotate.execute()

        angle = self.object.get_angle()
        change_velocity = ChangeVelocityCommand(self.object, float(angle.value))
        change_velocity.execute()
