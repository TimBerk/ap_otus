from queue import Queue

from server.cmd.log import LogCommand, handler_log


def test_success_log_command(exception, loguru_log):
    """Тестирование работы команды логирования"""
    test_command = LogCommand(exception)

    test_command.execute()

    assert str(exception) in loguru_log.text


def test_handle_log_add_command(exception):
    """Тестирование добавления исключения в очередь команд"""
    cmd_queue = Queue()

    handler_log(exception, cmd_queue)

    assert cmd_queue.qsize() == 1
