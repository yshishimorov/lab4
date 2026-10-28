"""
Тесты для задания средней сложности №1: Вычисление квадратов с помощью map.
"""

import unittest
from src.task1_squares_map import (
    calculate_squares,
    get_squares_map,
    квадраты_чисел,
)


class TestSquaresMap(unittest.TestCase):
    """Набор тестов для функции вычисления квадратов чисел через map."""

    def test_default_range_one_to_ten(self) -> None:
        """Проверка вычисления квадратов от 1 до 10."""
        expected = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        self.assertEqual(get_squares_map(1, 10), expected)
        self.assertEqual(get_squares_map(), expected)

    def test_custom_range(self) -> None:
        """Проверка вычисления квадратов произвольного диапазона."""
        self.assertEqual(get_squares_map(3, 6), [9, 16, 25, 36])
        self.assertEqual(get_squares_map(-3, 3), [9, 4, 1, 0, 1, 4, 9])
        self.assertEqual(get_squares_map(5, 5), [25])

    def test_calculate_squares_arbitrary_iterable(self) -> None:
        """Проверка работы с произвольными итерируемыми объектами."""
        nums = [2, 7, 12]
        self.assertEqual(calculate_squares(nums), [4, 49, 144])
        self.assertEqual(calculate_squares([]), [])
        self.assertEqual(calculate_squares((3, 4)), [9, 16])

    def test_invalid_range_order(self) -> None:
        """Проверка возбуждения ValueError при некорректном диапазоне."""
        with self.assertRaises(ValueError):
            get_squares_map(10, 1)

    def test_invalid_types(self) -> None:
        """Проверка валидации входных типов."""
        with self.assertRaises(TypeError):
            get_squares_map("1", 10)  # type: ignore
        with self.assertRaises(TypeError):
            get_squares_map(1, "10")  # type: ignore
        with self.assertRaises(TypeError):
            get_squares_map(1.5, 5)  # type: ignore
        with self.assertRaises(TypeError):
            calculate_squares(123)  # type: ignore

    def test_alias(self) -> None:
        """Проверка русскоязычного псевдонима."""
        self.assertIs(квадраты_чисел, get_squares_map)


if __name__ == "__main__":
    unittest.main()
