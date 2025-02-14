from queue import Queue

import pytest

from server.cmd.macros import MacrosCommand
from server.cmd.move import MoveCommand
from server.cmd.refuel import BurnFuelCommand, CheckFuelCommand
from server.errors import ErrorCommandException
from server.logic.movable import Move
from server.logic.refuelinge import Refueling
from server.models import Vector


def test_execute(space_ship):
    move_obj = Move(space_ship)
    refuel_obj = Refueling(space_ship)
    queue = Queue()
    queue.put(CheckFuelCommand(refuel_obj))
    queue.put(MoveCommand(move_obj))
    queue.put(BurnFuelCommand(refuel_obj))
    command = MacrosCommand(queue)

    command.execute()

    assert refuel_obj.get_fuel() == 9
    assert move_obj.get_position() == Vector(5, 8)


def test_error_execute(space_ship):
    space_ship.fuel = 0
    move_obj = Move(space_ship)
    refuel_obj = Refueling(space_ship)
    queue = Queue()
    queue.put(CheckFuelCommand(refuel_obj))
    queue.put(MoveCommand(move_obj))
    queue.put(BurnFuelCommand(refuel_obj))
    command = MacrosCommand(queue)

    with pytest.raises(ErrorCommandException):
        command.execute()
