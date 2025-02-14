from queue import Queue

import zope
from loguru import logger

from server.interfaces.cmd import ICommand


@zope.interface.implementer(ICommand)
class CommandLog:
    """
    Реализация команды логирования посредствам решения loguru.
    """

    def __init__(self, exception: Exception):
        self.exception = exception

    def execute(self):
        logger.warning(self.exception)


def handler_log(exception: Exception, cmd_q: Queue):
    """Обработчик для добавления исключения в виде команды в очередь"""

    new_command = CommandLog(exception)
    cmd_q.put(new_command)
