"""
Лабораторная работа №4. Задание средней сложности №3.
Сумма чисел с использованием функции reduce.
"""

from functools import reduce
from typing import Iterable, Optional, Union

Number = Union[int, float]


def sum_reduce(numbers: Iterable[Number], initial: Optional[Number] = None) -> Number:
    """Вычисляет сумму элементов последовательности с использованием functools.reduce.

    Свёртка осуществляется бинарной операцией сложения (lambda acc, x: acc + x).

    Args:
        numbers (Iterable[Number]): Последовательность чисел для суммирования.
        initial (Number, optional): Начальное значение аккумулятора.

    Returns:
        Number: Сумма всех элементов последовательности.

    Raises:
        TypeError: Если numbers не является итерируемым объектом или элементы не числа.
    """
    if not isinstance(numbers, Iterable):
        raise TypeError(f"Ожидался итерируемый объект чисел, получен: {type(numbers).__name__}.")

    nums_list = list(numbers)

    # Проверяем, что все элементы являются числами
    for idx, item in enumerate(nums_list):
        if not isinstance(item, (int, float)) or isinstance(item, bool):
            raise TypeError(f"Элемент на позиции {idx} не является числом: {item!r} ({type(item).__name__}).")

    if not nums_list:
        return 0 if initial is None else initial

    if initial is not None:
        if not isinstance(initial, (int, float)) or isinstance(initial, bool):
            raise TypeError("Начальное значение initial должно быть числом.")
        return reduce(lambda acc, x: acc + x, nums_list, initial)

    return reduce(lambda acc, x: acc + x, nums_list)


def sum_positive_reduce(numbers: Iterable[Number]) -> Number:
    """Вычисляет сумму только положительных чисел из переданной последовательности.

    Демонстрирует совместное применение filter и reduce.
    """
    positive_numbers = filter(lambda x: x > 0, numbers)
    return sum_reduce(positive_numbers, initial=0)


# Русскоязычные псевдонимы для совместимости
сумма_reduce = sum_reduce
сумма_положительных_reduce = sum_positive_reduce
