import zope.interface

from server.models import Vector


class IMovable(zope.interface.Interface):

    def get_velocity(self) -> Vector:
        """Получение позиции"""
        ...

    def get_position(self) -> Vector:
        """Получение позиции"""
        ...

    def set_position(self, new_value: Vector) -> None:
        """Установка позиции"""
        ...
