from queue import Queue

import zope

from server.errors import ErrorCommandException
from server.interfaces.cmd import ICommand


@zope.interface.implementer(ICommand)
class MacrosCommand:
    """Макрокоманда"""

    def __init__(self, queue: Queue[ICommand]):
        self.queue = queue

    def execute(self) -> None:
        while self.queue.qsize() > 0:
            try:
                current_command = self.queue.get()
                current_command.execute()
            except Exception as e:
                raise ErrorCommandException() from e
