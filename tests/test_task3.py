"""
Тесты для задания средней сложности №5: Генератор чисел Фибоначчи.
"""

import types
import unittest
from src.task3_fibonacci import (
    fibonacci_generator,
    fibonacci_up_to_value,
    get_fibonacci_list,
    генератор_фибоначчи,
)


class TestFibonacci(unittest.TestCase):
    """Набор тестов для генератора чисел Фибоначчи."""

    def test_generator_type(self) -> None:
        """Проверка, что функция возвращает объект-генератор."""
        gen = fibonacci_generator()
        self.assertIsInstance(gen, types.GeneratorType)

    def test_known_fibonacci_values(self) -> None:
        """Проверка значений первых 10 чисел Фибоначчи."""
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        self.assertEqual(get_fibonacci_list(10), expected)

    def test_edge_counts(self) -> None:
        """Проверка граничных значений количества чисел."""
        self.assertEqual(get_fibonacci_list(0), [])
        self.assertEqual(get_fibonacci_list(1), [0])
        self.assertEqual(get_fibonacci_list(2), [0, 1])

    def test_fibonacci_up_to_value(self) -> None:
        """Проверка генерации чисел до заданного максимального значения."""
        nums = list(fibonacci_up_to_value(30))
        self.assertEqual(nums, [0, 1, 1, 2, 3, 5, 8, 13, 21])
        self.assertEqual(list(fibonacci_up_to_value(0)), [0])
        self.assertEqual(list(fibonacci_up_to_value(-5)), [])

    def test_invalid_arguments(self) -> None:
        """Проверка валидации параметров."""
        with self.assertRaises(ValueError):
            list(fibonacci_generator(-5))
        with self.assertRaises(TypeError):
            list(fibonacci_generator("10"))  # type: ignore
        with self.assertRaises(TypeError):
            list(fibonacci_generator(3.14))  # type: ignore

    def test_alias(self) -> None:
        """Проверка русскоязычного псевдонима."""
        self.assertIs(генератор_фибоначчи, fibonacci_generator)


if __name__ == "__main__":
    unittest.main()
