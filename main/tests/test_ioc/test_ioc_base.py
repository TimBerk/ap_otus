from server.cmd.move import MoveCommand
from server.logic.movable import Move
from server.models import Vector


def test_register_and_resolve(ioc, space_ship):
    ioc.resolve("IoC.Register", "forward", MoveCommand)

    ioc.resolve("forward", Move(space_ship)).execute()

    assert space_ship.position == Vector(5, 8)


def test_scopes(ioc, space_ship):
    ioc.resolve("Scopes.New", "scope1")
    ioc.resolve("Scopes.Current", "scope1")
    ioc.resolve("IoC.Register", "forward", MoveCommand)

    ioc.resolve("forward", Move(space_ship)).execute()

    assert space_ship.position == Vector(5, 8)
