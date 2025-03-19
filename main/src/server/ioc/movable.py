class IoCMovable:
    @staticmethod
    def resolve(key, *args):
        operations = {
            'Spaceship.Operations.IMovable:velocity.get': IoCMovable._get_velocity,
            'Spaceship.Operations.IMovable:velocity.set': IoCMovable._set_velocity,
            'Spaceship.Operations.IMovable:position.get': IoCMovable._get_position,
            'Spaceship.Operations.IMovable:position.set': IoCMovable._set_position,
            'Adapter': IoCMovable._create_adapter,
            'Spaceship.Operations.IMovable:finish': IoCMovable._finish,
        }

        if key in operations:
            return operations[key](*args)

        raise ValueError(f'Unknown key: {key}')

    @staticmethod
    def _get_velocity(obj):
        return obj.velocity

    @staticmethod
    def _set_velocity(obj, value):
        obj.velocity = value
        return obj.velocity

    @staticmethod
    def _get_position(obj):
        return obj.position

    @staticmethod
    def _set_position(obj, value):
        obj.position = value
        return obj.position

    @staticmethod
    def _create_adapter(movable_type, obj):
        return movable_type(obj)

    @staticmethod
    def _finish(obj):
        obj.is_active = False
        return obj
