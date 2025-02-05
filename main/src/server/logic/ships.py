from server.models import Angle, Vector


class SpaceShip:

    def __init__(self,
                 id: int,
                 position: Vector | None = None,
                 velocity: Vector | None = None,
                 alpha: Angle | None = None,
                 angular_velocity: int | None = None):
        """

        :param id: идентификатор
        :param position: расположение
        :param velocity: скорость
        :param alpha: угол
        :param angular_velocity: угловая скорость
        """
        self.id = id
        self.position = position
        self.velocity = velocity
        self.alpha = alpha
        self.angular_velocity = angular_velocity
