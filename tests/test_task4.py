"""
Тесты для задания повышенной сложности №1: Композиция функций (compose).
"""

import unittest
from src.task4_compose import (
    compose,
    pipe,
    композиция,
)


class TestCompose(unittest.TestCase):
    """Набор тестов для функции compose и pipe."""

    def test_basic_compose(self) -> None:
        """Проверка порядка вычисления f(g(x))."""
        f = lambda x: x * 2
        g = lambda x: x + 3

        # compose(f, g)(4) == f(g(4)) == (4 + 3) * 2 = 14
        h = compose(f, g)
        self.assertEqual(h(4), 14)

    def test_three_functions_compose(self) -> None:
        """Проверка цепочки из трёх функций f(g(h(x)))."""
        f = lambda x: str(x)
        g = lambda x: x ** 2
        h = lambda x: x - 1

        composed = compose(f, g, h)
        # При x = 5: h(5) = 4, g(4) = 16, f(16) = "16"
        self.assertEqual(composed(5), "16")

    def test_pipe_left_to_right(self) -> None:
        """Проверка конвейера pipe: h(g(f(x)))."""
        f = lambda x: x * 2
        g = lambda x: x + 3

        # pipe(f, g)(4) == g(f(4)) == (4 * 2) + 3 = 11
        piped = pipe(f, g)
        self.assertEqual(piped(4), 11)

    def test_multiple_arguments_on_first_function(self) -> None:
        """Проверка передачи нескольких аргументов в первую функцию цепочки."""
        add = lambda a, b: a + b
        square = lambda x: x ** 2

        comp = compose(square, add)
        # square(add(2, 3)) == 5 ** 2 = 25
        self.assertEqual(comp(2, 3), 25)

    def test_empty_compose_identity(self) -> None:
        """Проверка вызова без аргументов (тождественная функция)."""
        identity = compose()
        self.assertEqual(identity(42), 42)
        self.assertEqual(identity("строка"), "строка")

    def test_single_function(self) -> None:
        """Проверка композиции из одной функции."""
        fn = lambda x: x + 10
        self.assertEqual(compose(fn)(5), 15)

    def test_invalid_type_raises_typeerror(self) -> None:
        """Проверка валидации невызываемых аргументов."""
        with self.assertRaises(TypeError):
            compose(lambda x: x, "не_функция")  # type: ignore

    def test_alias(self) -> None:
        """Проверка русскоязычного псевдонима."""
        self.assertIs(композиция, compose)


if __name__ == "__main__":
    unittest.main()
