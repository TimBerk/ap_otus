import zope.interface

from server.models import Angle


class IRotatable(zope.interface.Interface):

    def get_angle(self) -> Angle:
        """Получение угла"""
        ...

    def set_angel(self, new_value: Angle):
        """Установка угла"""
        ...

    def get_division(self) -> int:
        """Получение основания"""
        ...

    def get_angular_velocity(self) -> int:
        """Получение угловой скорости"""
        ...
