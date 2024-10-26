import math


def validate_number(value):
    """Валидация числовых значений"""

    if isinstance(value, bytes | bytearray | str | list | set | dict):
        raise TypeError('Invalid data type')

    if value is None or math.isinf(value):
        raise ValueError('Incorrect value')


def solve(a: float, b: float, c: float, epsilon=1e-9) -> tuple[float | None, float | None]:
    """Поиск корней квадратного уравнения"""

    validate_number(a)
    validate_number(b)
    validate_number(c)

    if math.isclose(a, 0, abs_tol=epsilon):
        raise ValueError('The coefficient "a" cannot be equal to zero')

    discriminant: float = b ** 2 - 4 * a * c
    if math.isclose(discriminant, 0, abs_tol=epsilon):
        x = -b / (2 * a)
        return x, x
    elif discriminant < 0:
        return None, None

    sqrt_discriminant = discriminant ** 0.5
    x1 = (-b + sqrt_discriminant) / (2 * a)
    x2 = (-b - sqrt_discriminant) / (2 * a)

    return x1, x2
