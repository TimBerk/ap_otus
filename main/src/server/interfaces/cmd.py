import zope.interface


class ICommand(zope.interface.Interface):

    def execute(self):
        """Выполнение команды"""
        ...
