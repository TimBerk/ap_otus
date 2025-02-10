import zope.interface

from server.models import Vector


class IMovable(zope.interface.Interface):

    def get_velocity(self) -> Vector:
        """Получение вектора мгновенной скорости"""
        ...

    def set_velocity(self, value: Vector) -> None:
        """Установка вектора мгновенной скорости"""
        ...

    def get_position(self) -> Vector:
        """Получение позиции"""
        ...

    def set_position(self, value: Vector) -> None:
        """Установка позиции"""
        ...
