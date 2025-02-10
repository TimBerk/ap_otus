from server.logic.movable import Move
from server.models import Vector


def test_get_position(space_ship):
    move_obj = Move(space_ship)

    assert move_obj.get_position() == space_ship.position


def test_get_velocity(space_ship):
    move_obj = Move(space_ship)

    assert move_obj.get_velocity() == space_ship.velocity


def test_set_position(space_ship):
    new_position = Vector(1, 1)
    move_obj = Move(space_ship)

    move_obj.set_position(new_position)

    assert move_obj.get_position() == space_ship.position
