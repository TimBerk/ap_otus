import zope

from server.errors import BurnFuelParamCommandException, ErrorCommandException
from server.interfaces.cmd import ICommand


@zope.interface.implementer(ICommand)
class CheckFuelCommand:
    """Команда проверки топлива объекта"""

    def __init__(self, object):
        self.object = object

    def execute(self) -> None:
        if not self.object.check_fuel():
            raise ErrorCommandException()
        return


@zope.interface.implementer(ICommand)
class BurnFuelCommand:
    """Команда расхода топлива объекта"""

    def __init__(self, object):
        self.object = object

    def execute(self) -> None:
        fuel = self.object.get_fuel()
        if not isinstance(fuel, int):
            raise BurnFuelParamCommandException('Incorrect fuel value')

        rate_of_fuel = self.object.get_rate_of_fuel()
        if not isinstance(rate_of_fuel, int):
            raise BurnFuelParamCommandException('Incorrect rate of fuel value')

        fuel -= rate_of_fuel
        if fuel < 0:
            raise BurnFuelParamCommandException('Incorrect new fuel value')

        self.object.set_fuel(fuel)
