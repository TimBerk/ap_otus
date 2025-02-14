from queue import Queue

import zope

from server.errors import RepeatCommandException
from server.interfaces.cmd import ICommand


@zope.interface.implementer(ICommand)
class RepeatCommand:
    """
    Реализация команды повтор.
    При достижении максимального количества повторов выбрасывается исключение  RepeatCommandException
    """

    def __init__(self, cmd: ICommand, max_retries: int):
        self.cmd = cmd
        self.max_retries = max_retries
        self.count = 0

    def execute(self):
        if self.count >= self.max_retries:
            raise RepeatCommandException(f'The command could not repeat: {self.max_retries} times')

        self.count += 1
        self.cmd.execute()


def handler_repeat(cmd: ICommand, max_retries, cmd_q: Queue):
    """Обработчик для повторного добавления команды в очередь"""

    if not isinstance(cmd, RepeatCommand):
        cmd = RepeatCommand(cmd, max_retries)
    cmd_q.put(cmd)
