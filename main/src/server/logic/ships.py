from server.models import Angle, Vector


class SpaceShip:

    def __init__(self,
                 id: int,
                 position: Vector | None = None,
                 velocity: Vector | None = None,
                 alpha: Angle | None = None,
                 angular_velocity: int | None = None,
                 fuel: int | None = None,
                 rate_of_fuel: int | None = None):
        """

        :param id: идентификатор
        :param position: расположение
        :param velocity: скорость
        :param alpha: угол
        :param angular_velocity: угловая скорость
        :param fuel: уровень топлива
        :param rate_of_fuel: расход топлива
        """
        self.id = id
        self.position = position
        self.velocity = velocity
        self.alpha = alpha
        self.angular_velocity = angular_velocity
        self.fuel = fuel
        self.rate_of_fuel = rate_of_fuel
