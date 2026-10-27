"""
Лабораторная работа №4. Задание средней сложности №5.
Создать генератор чисел Фибоначчи с использованием оператора yield.
"""

from typing import Generator, List, Optional


def fibonacci_generator(count: Optional[int] = None) -> Generator[int, None, None]:
    """Генератор последовательности чисел Фибоначчи.

    Последовательность начинается с 0, 1, 1, 2, 3, 5, 8, 13, ...
    Использует отложенные вычисления (lazy evaluation) через yield.

    Args:
        count (int, optional): Количество чисел для генерации. Если None, генерирует бесконечно.

    Yields:
        int: Очередное число Фибоначчи.

    Raises:
        TypeError: Если count не целое число.
        ValueError: Если count отрицательный.
    """
    if count is not None:
        if not isinstance(count, int) or isinstance(count, bool):
            raise TypeError(f"Количество чисел должно быть целым числом, получено: {type(count).__name__}.")
        if count < 0:
            raise ValueError(f"Количество чисел не может быть отрицательным: {count}.")
        if count == 0:
            return

    a, b = 0, 1
    generated = 0

    while count is None or generated < count:
        yield a
        a, b = b, a + b
        generated += 1


def fibonacci_up_to_value(max_value: int) -> Generator[int, None, None]:
    """Генерирует числа Фибоначчи, значение которых не превышает max_value.

    Args:
        max_value (int): Максимальное пороговое значение.

    Yields:
        int: Числа Фибоначчи <= max_value.
    """
    if not isinstance(max_value, int) or isinstance(max_value, bool):
        raise TypeError("Пороговое значение должно быть целым числом.")
    if max_value < 0:
        return

    a, b = 0, 1
    while a <= max_value:
        yield a
        a, b = b, a + b


def get_fibonacci_list(count: int) -> List[int]:
    """Возвращает список первых count чисел Фибоначчи."""
    return list(fibonacci_generator(count))


# Русскоязычные псевдонимы для совместимости
генератор_фибоначчи = fibonacci_generator
числа_фибоначчи_до = fibonacci_up_to_value
список_фибоначчи = get_fibonacci_list
