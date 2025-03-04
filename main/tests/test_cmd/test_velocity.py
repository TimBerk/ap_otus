import pytest

from server.cmd.velocity import ChangeVelocityCommand, RotateVelocityCommand
from server.errors import ChangeVelocityCommandException, RotateParamException
from server.logic.mixins import MoveRotate
from server.models import Vector


def test_change_execute(space_ship):
    move_rotate_obj = MoveRotate(space_ship)
    command = ChangeVelocityCommand(move_rotate_obj, 90)

    command.execute()

    assert move_rotate_obj.get_velocity() == Vector(0, -8)


def test_error_change_velocity(space_ship):
    space_ship.velocity = None
    move_rotate_obj = MoveRotate(space_ship)
    command = ChangeVelocityCommand(move_rotate_obj, 90)

    with pytest.raises(ChangeVelocityCommandException):
        command.execute()


def test_rotate_execute(space_ship):
    move_rotate_obj = MoveRotate(space_ship)
    command = RotateVelocityCommand(move_rotate_obj)

    command.execute()

    assert move_rotate_obj.get_velocity() == Vector(0, -8)
    assert move_rotate_obj.get_position() == Vector(x=12, y=5)


def test_rotate_with_zero_velocity_execute(space_ship):
    space_ship.velocity = Vector(0, 0)
    move_rotate_obj = MoveRotate(space_ship)
    command = RotateVelocityCommand(move_rotate_obj)

    command.execute()

    assert move_rotate_obj.get_velocity() == Vector(0, 0)
    assert move_rotate_obj.get_position() == Vector(x=12, y=5)


def test_error_rotate_angle(space_ship):
    space_ship.alpha = None
    move_rotate_obj = MoveRotate(space_ship)
    command = RotateVelocityCommand(move_rotate_obj)

    with pytest.raises(RotateParamException):
        command.execute()


def test_error_rotate_angular_velocity(space_ship):
    space_ship.angular_velocity = None
    move_rotate_obj = MoveRotate(space_ship)
    command = RotateVelocityCommand(move_rotate_obj)

    with pytest.raises(RotateParamException):
        command.execute()


def test_error_rotate_velocity(space_ship):
    space_ship.velocity = None
    move_rotate_obj = MoveRotate(space_ship)
    command = RotateVelocityCommand(move_rotate_obj)

    with pytest.raises(ChangeVelocityCommandException):
        command.execute()
