import pytest

from server.adapters.movable import MovableAdapter
from server.models import Vector


@pytest.fixture
def movable_adapter(space_ship, ioc_movable):
    # Создаем объект UObject с начальными значениями
    space_ship.position = Vector(0, 0)
    space_ship.velocity = Vector(1, 1)
    return ioc_movable.resolve("Adapter", MovableAdapter, space_ship)


def test_get_velocity(movable_adapter):
    # Проверяем, что getVelocity возвращает вектор мгновенной скорости
    velocity = movable_adapter.get_velocity()

    assert velocity.x == 1
    assert velocity.y == 1


def test_set_velocity(movable_adapter):
    # Проверяем, что setVelocity устанавливает вектор мгновенной скорости
    velocity = movable_adapter.set_velocity(Vector(10, 10))

    assert velocity.x == 10
    assert velocity.y == 10


def test_get_position(movable_adapter):
    # Проверяем, что getPosition возвращает правильное значение
    position = movable_adapter.get_position()

    assert position.x == 0
    assert position.y == 0


def test_set_position(movable_adapter):
    # Устанавливаем новое положение
    movable_adapter.set_position(Vector(10, 10))

    position = movable_adapter.get_position()
    assert position.x == 10
    assert position.y == 10


def test_finish(movable_adapter):
    # Проверяем активность корабля после финиша
    obj = movable_adapter.finish()

    assert not obj.is_active
