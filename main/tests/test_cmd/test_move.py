import pytest

from server.cmd.move import MoveCommand
from server.errors import MoveParamException
from server.logic.movable import Move
from server.logic.ships import SpaceShip
from server.models import Vector


def test_change_position():
    space_ship = SpaceShip(1, position=Vector(12, 5), velocity=Vector(-7, 3))
    move_obj = Move(space_ship)
    command = MoveCommand(move_obj)

    command.execute()

    assert move_obj.get_position() == Vector(5, 8)


def test_move_with_incorrect_location_raise_error():
    space_ship = SpaceShip(1, None, Vector(1, 1))
    move_obj = Move(space_ship)
    command = MoveCommand(move_obj)

    with pytest.raises(MoveParamException, match='Incorrect position value'):
        command.execute()


def test_move_with_incorrect_velocity_raise_error():
    space_ship = SpaceShip(1, Vector(0, 0), None)
    move_obj = Move(space_ship)
    command = MoveCommand(move_obj)

    with pytest.raises(MoveParamException, match='Incorrect velocity value'):
        command.execute()


def test_move_with_incorrect_new_vector_raise_error():
    space_ship = SpaceShip(1, Vector(0, 0), Vector(0, 'test'))
    move_obj = Move(space_ship)
    command = MoveCommand(move_obj)

    with pytest.raises(TypeError):
        command.execute()
