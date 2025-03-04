import zope.interface

from server.interfaces.refuelinge import IRefueling


@zope.interface.implementer(IRefueling)
class Refueling:

    def __init__(self, object):
        self.object = object

    def get_fuel(self) -> int:
        return self.object.fuel

    def set_fuel(self, value) -> None:
        self.object.fuel = value

    def get_rate_of_fuel(self) -> int:
        return self.object.rate_of_fuel

    def check_fuel(self) -> bool:
        return self.get_fuel() > 0
