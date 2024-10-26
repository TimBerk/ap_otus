import math

import pytest

from utils import solve

ERROR_TYPE_TEXT = 'Invalid data type'
ERROR_VALUE_TEXT = 'Incorrect value'
ERROR_CASES = [
    (b'1', ERROR_TYPE_TEXT),
    (bytearray(b'1'), ERROR_TYPE_TEXT),
    ('1', ERROR_TYPE_TEXT),
    ([1], ERROR_TYPE_TEXT),
    ({1}, ERROR_TYPE_TEXT),
    ({1: 1}, ERROR_TYPE_TEXT),
    (None, ERROR_VALUE_TEXT),
    (float('inf'), ERROR_VALUE_TEXT),
    (float('-inf'), ERROR_VALUE_TEXT),
]


class TestSolve:

    def test_solve_quadratic_equation_empty_result(self):
        """Тест для кейса x^2+1 = 0 корней нет"""

        roots = solve(1, 0, 1)

        assert roots == (None, None)

    def test_solve_quadratic_equation_result_has_2_root(self):
        """Тест для кейса x^2-1 = 0 есть два корня"""

        roots = solve(1, 0, -1)

        assert roots == (1, -1)

    def test_solve_quadratic_equation_result_has_1_root(self):
        """Тест для кейса x^2+2x+1 = 0 есть один корень"""

        roots = solve(1, 2, 1)

        assert roots == (-1, -1)

    def test_solve_quadratic_equation_with_zero_raise_value_error(self):
        """Тест для кейса a = 0 - выбрасывается исключение"""

        with pytest.raises(ValueError) as exc_info:
            solve(0, 2, 3)

        assert str(exc_info.value) == 'The coefficient "a" cannot be equal to zero'

    def test_solve_quadratic_equation_with_small_non_zero_discriminant(self):
        """Тест на корректное вычисление корня, если дискриминант близок к нулю, но не равен ему точно."""

        roots = solve(1, 2, 1 + 1e-15)  # Дискриминант будет очень маленьким, но не равным нулю

        assert math.isclose(roots[0], -1, abs_tol=1e-9)
        assert math.isclose(roots[1], -1, abs_tol=1e-9)

    @pytest.mark.parametrize('value,error_text', ERROR_CASES)
    def test_solve_quadratic_equation_with_incorrect_type_or_value(self, value, error_text):
        """Тест на вызов исключения при некорректном типе/значении одного из параметра."""

        params = [
            {'a': value, 'b': 2, 'c': 1},
            {'a': 1, 'b': value, 'c': 1},
            {'a': 1, 'b': 2, 'c': value},
        ]

        for case in params:
            with pytest.raises((TypeError, ValueError,)) as exc_info:
                solve(**case)

            assert str(exc_info.value) == error_text
