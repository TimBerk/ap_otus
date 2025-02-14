from queue import Queue

import zope

from server.cmd.macros import MacrosCommand
from server.interfaces.cmd import ICommand


@zope.interface.implementer(ICommand)
class ForwardMotionCommand:
    """Макрокоманда длительного движения по прямой"""

    def __init__(self, check, move, burn):
        self._queue = Queue()
        self._queue.put(check)
        self._queue.put(move)
        self._queue.put(burn)
        self.macros = MacrosCommand(self._queue)

    def execute(self) -> None:
        self.macros.execute()
