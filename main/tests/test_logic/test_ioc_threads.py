import threading

from server.cmd.move import MoveCommand
from server.cmd.refuel import BurnFuelCommand
from server.logic.ioc import IoCContainer
from server.logic.movable import Move
from server.logic.refuelinge import Refueling
from server.logic.ships import SpaceShip
from server.models import Angle, Vector


def space_ship_factory(id_ship: int) -> SpaceShip:
    return SpaceShip(
        id=id_ship,
        position=Vector(12, 5),
        velocity=Vector(-7, 3),
        alpha=Angle(0, 360),
        angular_velocity=90,
        fuel=10,
        rate_of_fuel=1,
    )


def thread_runner(worker):
    threads = []
    for i in range(2):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


def test_thread_local_scopes(ioc):
    def worker(thread_id):
        space_ship = space_ship_factory(thread_id)
        ioc.resolve('Scopes.New', f'scope_local_{thread_id}')
        ioc.resolve('Scopes.Current', f'scope_local_{thread_id}')
        ioc.resolve('IoC.Register', 'forward', MoveCommand)

        ioc.resolve('forward', Move(space_ship)).execute()

        assert space_ship.position == Vector(5, 8)

    thread_runner(worker)


def test_global_scope_in_threads(ioc):
    ioc.resolve('IoC.Register', 'scope_global', lambda args: 'Global')
    ioc.resolve('IoC.Register', 'forward', MoveCommand)

    def worker(thread_id):
        space_ship = space_ship_factory(thread_id)
        ioc.resolve('forward', Move(space_ship)).execute()
        assert space_ship.position == Vector(5, 8)

    thread_runner(worker)


def test_mixed_scopes():
    ioc = IoCContainer()
    ioc.resolve('IoC.Register', 'scope_global', lambda args: 'Global')
    ioc.resolve('IoC.Register', 'forward', MoveCommand)

    def worker(thread_id):
        space_ship = space_ship_factory(thread_id)
        ioc.resolve('Scopes.New', f'scope_local_{thread_id}')
        ioc.resolve('Scopes.Current', f'scope_local_{thread_id}')
        ioc.resolve('IoC.Register', 'burn_fuel', BurnFuelCommand)

        ioc.resolve('burn_fuel', Refueling(space_ship)).execute()
        assert space_ship.fuel == 9
        assert space_ship.position == Vector(12, 5)

        ioc.resolve('Scopes.Current', 'scope_global')
        ioc.resolve('forward', Move(space_ship)).execute()
        assert space_ship.fuel == 9
        assert space_ship.position == Vector(5, 8)

    thread_runner(worker)
