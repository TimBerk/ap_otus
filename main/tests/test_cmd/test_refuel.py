import pytest

from server.cmd.refuel import BurnFuelCommand, CheckFuelCommand
from server.errors import BurnFuelParamCommandException, ErrorCommandException
from server.logic.refuelinge import Refueling


def test_check_execute(space_ship):
    refuel_obj = Refueling(space_ship)
    command = CheckFuelCommand(refuel_obj)

    command.execute()


def test_error_check_execute(space_ship):
    space_ship.fuel = 0
    refuel_obj = Refueling(space_ship)
    command = CheckFuelCommand(refuel_obj)

    with pytest.raises(ErrorCommandException):
        command.execute()


def test_burn_execute(space_ship):
    refuel_obj = Refueling(space_ship)
    command = BurnFuelCommand(refuel_obj)

    command.execute()

    assert refuel_obj.get_fuel() == 9


def test_error_burn_fuel_param(space_ship):
    space_ship.fuel = None
    refuel_obj = Refueling(space_ship)
    command = BurnFuelCommand(refuel_obj)

    with pytest.raises(BurnFuelParamCommandException):
        command.execute()


def test_error_burn_rate_of_fuel_param(space_ship):
    space_ship.rate_of_fuel = None
    refuel_obj = Refueling(space_ship)
    command = BurnFuelCommand(refuel_obj)

    with pytest.raises(BurnFuelParamCommandException):
        command.execute()


def test_error_burn_new_fuel_param(space_ship):
    space_ship.rate_of_fuel = 20
    refuel_obj = Refueling(space_ship)
    command = BurnFuelCommand(refuel_obj)

    with pytest.raises(BurnFuelParamCommandException):
        command.execute()
