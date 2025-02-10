from server.logic.rotatable import Rotate
from server.models import Angle


def test_get_angle(space_ship):
    rotate_obj = Rotate(space_ship)

    assert rotate_obj.get_angle() == space_ship.alpha


def test_set_angle(space_ship):
    new_angle = Angle(90, 360)
    rotate_obj = Rotate(space_ship)

    rotate_obj.set_angle(new_angle)

    assert rotate_obj.get_angle() == new_angle


def test_get_division(space_ship):
    rotate_obj = Rotate(space_ship)

    assert rotate_obj.get_division() == space_ship.alpha.division


def test_get_angular_velocity(space_ship):
    rotate_obj = Rotate(space_ship)

    assert rotate_obj.get_angular_velocity() == space_ship.angular_velocity
