import pytest

from server.errors import RotateParamException
from server.logic.rotable import Rotate
from server.logic.ships import SpaceShip
from server.models import Angle, Vector


def test_change_angel():
    space_ship = SpaceShip(1, None, None, Angle(0, 10), 10)
    rotate_obj = Rotate(space_ship)

    rotate_obj.execute()

    assert rotate_obj.get_angle() == 0


def test_rotate_with_incorrect_angle_raise_error():
    space_ship = SpaceShip(1, None, None, None, 10)
    rotate_obj = Rotate(space_ship)

    with pytest.raises(RotateParamException, match='Incorrect alpha value'):
        rotate_obj.execute()


def test_rotate_with_incorrect_angular_velocity_raise_error():
    space_ship = SpaceShip(1, Vector(0, 0), None, Angle(0, 10), None)
    rotate_obj = Rotate(space_ship)

    with pytest.raises(RotateParamException, match='Incorrect angular velocity value'):
        rotate_obj.execute()


def test_rotate_with_incorrect_new_angle_raise_error():
    space_ship = SpaceShip(1, None, None, Angle('test', 10), 10)
    rotate_obj = Rotate(space_ship)

    with pytest.raises(TypeError):
        rotate_obj.execute()
