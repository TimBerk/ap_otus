import zope

from server.interfaces.movable import IMovable
from server.ioc.movable import IoCMovable


@zope.interface.implementer(IMovable)
class MovableAdapter:
    def __init__(self, obj):
        self.obj = obj

    def get_velocity(self):
        return IoCMovable.resolve("Spaceship.Operations.IMovable:velocity.get", self.obj)

    def set_velocity(self, value):
        return IoCMovable.resolve("Spaceship.Operations.IMovable:velocity.set", self.obj, value)

    def get_position(self):
        return IoCMovable.resolve("Spaceship.Operations.IMovable:position.get", self.obj)

    def set_position(self, value):
        return IoCMovable.resolve("Spaceship.Operations.IMovable:position.set", self.obj, value)

    def finish(self):
        return IoCMovable.resolve("Spaceship.Operations.IMovable:finish", self.obj)
