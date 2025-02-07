import pytest
import zope
from loguru import logger

from server.interfaces.cmd import ICommand


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
