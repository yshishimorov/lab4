"""
Лабораторная работа №4. Задание средней сложности №1.
Вычислить квадраты чисел 1–10 с использованием функции map.
"""

from typing import Iterable, List


def get_squares_map(start: int = 1, end: int = 10) -> List[int]:
    """Вычисляет квадраты чисел в диапазоне от start до end включительно.

    Использует встроенную функцию высшего порядка map и анонимную лямбда-функцию.

    Args:
        start (int): Начало диапазона (по умолчанию 1).
        end (int): Конец диапазона (по умолчанию 10).

    Returns:
        List[int]: Список квадратов чисел.

    Raises:
        TypeError: Если аргументы не являются целыми числами.
        ValueError: Если start > end.
    """
    if not isinstance(start, int) or isinstance(start, bool):
        raise TypeError(f"Начало диапазона должно быть целым числом, получено: {type(start).__name__}.")
    if not isinstance(end, int) or isinstance(end, bool):
        raise TypeError(f"Конец диапазона должен быть целым числом, получено: {type(end).__name__}.")
    if start > end:
        raise ValueError(f"Начало диапазона ({start}) не может быть больше конца ({end}).")

    return list(map(lambda x: x ** 2, range(start, end + 1)))


def calculate_squares(numbers: Iterable[int]) -> List[int]:
    """Применяет map для вычисления квадратов произвольной последовательности чисел.

    Args:
        numbers (Iterable[int]): Итерируемый объект с числами.

    Returns:
        List[int]: Список квадратов переданных чисел.
    """
    if not isinstance(numbers, Iterable):
        raise TypeError("Аргумент numbers должен быть итерируемым объектом.")

    return list(map(lambda x: x ** 2, numbers))


# Русскоязычные псевдонимы для совместимости
квадраты_чисел = get_squares_map
вычислить_квадраты = calculate_squares
