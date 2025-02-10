from queue import Queue

import pytest

from server.cmd.repeat import RepeatCommand, handler_repeat
from server.errors import RepeatCommandException


def test_success_repeat_command(success_command, capsys):
    """Тестирование успешной работы команды повтора"""
    cmd_repeat = RepeatCommand(success_command, 1)

    cmd_repeat.execute()

    captured = capsys.readouterr()
    assert 'Test Success Command' in captured.out
    assert cmd_repeat.count == 1


def test_error_repeat_command_without_retries(success_command, capsys):
    """Тестирование исключения при указании 0 количества повторов"""
    cmd_repeat = RepeatCommand(success_command, 0)

    with pytest.raises(RepeatCommandException):
        cmd_repeat.execute()


def test_handle_repeat_add_command(success_command):
    """Тестирование добавления команды в очередь команд"""
    cmd_queue = Queue()

    handler_repeat(success_command, 1, cmd_queue)

    assert cmd_queue.qsize() == 1
