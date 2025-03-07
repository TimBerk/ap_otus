import pytest
import zope
from loguru import logger

from server.interfaces.cmd import ICommand
from server.logic.ioc import IoCContainer
from server.logic.ships import SpaceShip
from server.models import Angle, Vector


@zope.interface.implementer(ICommand)
class TestSuccessCommand:

    def execute(self):
        print('Test Success Command')


@zope.interface.implementer(ICommand)
class TestErrorCommand:

    def __init__(self, exception):
        self.exception = exception

    def execute(self):
        raise Exception(self.exception)


@pytest.fixture(autouse=True)
def loguru_log(caplog):
    handler_id = logger.add(caplog.handler, format="{message}")
    yield caplog
    logger.remove(handler_id)


@pytest.fixture
def exception():
    return Exception('Test Error Command')


@pytest.fixture
def success_command():
    return TestSuccessCommand()


@pytest.fixture
def error_command(exception):
    return TestErrorCommand(exception)


@pytest.fixture
def space_ship():
    return SpaceShip(
        id=1,
        position=Vector(12, 5),
        velocity=Vector(-7, 3),
        alpha=Angle(0, 360),
        angular_velocity=90,
        fuel=10,
        rate_of_fuel=1,
    )


@pytest.fixture
def ioc():
    return IoCContainer()
