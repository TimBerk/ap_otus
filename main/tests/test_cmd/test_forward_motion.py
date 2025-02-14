import pytest

from server.cmd.forward_motion import ForwardMotionCommand
from server.cmd.move import MoveCommand
from server.cmd.refuel import BurnFuelCommand, CheckFuelCommand
from server.errors import ErrorCommandException
from server.logic.movable import Move
from server.logic.refuelinge import Refueling
from server.models import Vector


def test_execute(space_ship):
    move_obj = Move(space_ship)
    refuel_obj = Refueling(space_ship)
    check_command = CheckFuelCommand(refuel_obj)
    move_command = MoveCommand(move_obj)
    burn_command = BurnFuelCommand(refuel_obj)
    command = ForwardMotionCommand(check_command, move_command, burn_command)

    command.execute()

    assert refuel_obj.get_fuel() == 9
    assert move_obj.get_position() == Vector(5, 8)


def test_error_execute(space_ship):
    space_ship.fuel = 0
    move_obj = Move(space_ship)
    refuel_obj = Refueling(space_ship)
    check_command = CheckFuelCommand(refuel_obj)
    move_command = MoveCommand(move_obj)
    burn_command = BurnFuelCommand(refuel_obj)
    command = ForwardMotionCommand(check_command, move_command, burn_command)

    with pytest.raises(ErrorCommandException):
        command.execute()
