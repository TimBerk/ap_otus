from queue import Queue

import pytest

from server.cmd.log import handler_log
from server.cmd.repeat import handler_repeat
from server.errors import RepeatCommandException


@pytest.mark.parametrize('max_retries,count_actions', [(1, 4), (2, 5)])
def test_integration_cmd(max_retries, count_actions, error_command, loguru_log):
    """
    Тестирование автоматической обработки исключений
    с повтором команды и последующим добавлением лога для пунктов 8 и 9.
    Количество повторов определяется параметром max_retries для обработчика handler_repeat
    """

    queue = Queue()
    queue.put(error_command)
    counter = 0

    while queue.qsize() > 0:
        current_command = queue.get()
        try:
            current_command.execute()
        except Exception as e:
            if isinstance(e, RepeatCommandException):
                handler_log(e, queue)
            else:
                handler_repeat(current_command, max_retries, queue)
        counter += 1

    assert counter == count_actions
    assert f'The command could not repeat: {max_retries} times' in loguru_log.text
