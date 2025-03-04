from typing import TypeVar

from server.interfaces.movable import IMovable
from server.interfaces.rotatable import IRotatable

MovableRotatable = TypeVar('MovableRotatable', bound=IMovable and IRotatable)
