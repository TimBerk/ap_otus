import zope.interface


class IRefueling(zope.interface.Interface):

    def get_fuel(self) -> int:
        """Получение значения топлива"""
        ...

    def set_fuel(self, value) -> int:
        """Установка значения топлива"""
        ...

    def get_rate_of_flow(self) -> int:
        """Получение расхода топлива"""
        ...

    def check_fuel(self) -> bool:
        """Проверка наличия топлива"""
        ...
