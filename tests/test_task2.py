"""
Тесты для задания средней сложности №3: Суммирование чисел через reduce.
"""

import unittest
from src.task2_sum_reduce import (
    sum_positive_reduce,
    sum_reduce,
    сумма_reduce,
)


class TestSumReduce(unittest.TestCase):
    """Набор тестов для функции суммирования через reduce."""

    def test_basic_sum(self) -> None:
        """Проверка сложения целых чисел."""
        self.assertEqual(sum_reduce([1, 2, 3, 4, 5]), 15)
        self.assertEqual(sum_reduce([10]), 10)
        self.assertEqual(sum_reduce([-5, 5]), 0)

    def test_float_sum(self) -> None:
        """Проверка сложения вещественных чисел."""
        self.assertAlmostEqual(sum_reduce([1.5, 2.5, 3.0]), 7.0)

    def test_initial_value(self) -> None:
        """Проверка суммирования с начальным значением аккумулятора."""
        self.assertEqual(sum_reduce([1, 2, 3], initial=10), 16)
        self.assertEqual(sum_reduce([], initial=42), 42)

    def test_empty_sequence(self) -> None:
        """Проверка поведения на пустой последовательности (возврат 0)."""
        self.assertEqual(sum_reduce([]), 0)

    def test_sum_positive_reduce(self) -> None:
        """Проверка суммирования только положительных элементов."""
        data = [-10, 5, -2, 15, 0, -1]
        self.assertEqual(sum_positive_reduce(data), 20)
        self.assertEqual(sum_positive_reduce([-1, -2, -3]), 0)

    def test_invalid_arguments(self) -> None:
        """Проверка валидации некорректных типов."""
        with self.assertRaises(TypeError):
            sum_reduce(12345)  # type: ignore
        with self.assertRaises(TypeError):
            sum_reduce([1, "два", 3])  # type: ignore
        with self.assertRaises(TypeError):
            sum_reduce([1, 2], initial="ноль")  # type: ignore

    def test_alias(self) -> None:
        """Проверка русскоязычного псевдонима."""
        self.assertIs(сумма_reduce, sum_reduce)


if __name__ == "__main__":
    unittest.main()
