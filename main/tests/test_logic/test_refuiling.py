from server.logic.refuelinge import Refueling


def test_get_fuel(space_ship):
    rotate_obj = Refueling(space_ship)

    assert rotate_obj.get_fuel() == space_ship.fuel


def test_set_fuel(space_ship):
    new_fuel = 20
    rotate_obj = Refueling(space_ship)

    rotate_obj.set_fuel(new_fuel)

    assert rotate_obj.get_fuel() == new_fuel


def test_get_rate_of_flow(space_ship):
    rotate_obj = Refueling(space_ship)

    assert rotate_obj.get_rate_of_fuel() == space_ship.rate_of_fuel


def test_check_fuel(space_ship):
    rotate_obj = Refueling(space_ship)

    assert rotate_obj.check_fuel() is True


def test_check_fuel_is_false(space_ship):
    space_ship.fuel = 0
    rotate_obj = Refueling(space_ship)

    assert rotate_obj.check_fuel() is False
