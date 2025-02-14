import pytest

from server.cmd.rotate import RotateCommand
from server.errors import RotateParamException
from server.logic.rotatable import Rotate
from server.logic.ships import SpaceShip
from server.models import Angle, Vector


def test_change_angel():
    space_ship = SpaceShip(1, None, None, Angle(0, 10), 10)
    rotate_obj = Rotate(space_ship)
    command = RotateCommand(rotate_obj)

    command.execute()

    assert rotate_obj.get_angle() == space_ship.alpha


def test_rotate_with_incorrect_angle_raise_error():
    space_ship = SpaceShip(1, None, None, None, 10)
    rotate_obj = Rotate(space_ship)
    command = RotateCommand(rotate_obj)

    with pytest.raises(RotateParamException, match='Incorrect alpha value'):
        command.execute()


def test_rotate_with_incorrect_angular_velocity_raise_error():
    space_ship = SpaceShip(1, Vector(0, 0), None, Angle(0, 10), None)
    rotate_obj = Rotate(space_ship)
    command = RotateCommand(rotate_obj)

    with pytest.raises(RotateParamException, match='Incorrect angular velocity value'):
        command.execute()


def test_rotate_with_incorrect_new_angle_raise_error():
    space_ship = SpaceShip(1, None, None, Angle('test', 10), 10)
    rotate_obj = Rotate(space_ship)
    command = RotateCommand(rotate_obj)

    with pytest.raises(TypeError):
        command.execute()
