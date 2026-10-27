"""
Лабораторная работа №4. Задание повышенной сложности №1.
Композиция функций (compose).
"""

from functools import reduce
from typing import Any, Callable


def compose(*functions: Callable[..., Any]) -> Callable[..., Any]:
    """Создаёт композицию переданных функций (вычисление справа налево).

    Математическое определение: (f ∘ g ∘ h)(x) = f(g(h(x))).
    Первая функция (самая правая) может принимать произвольное число аргументов (*args, **kwargs),
    последующие функции принимают результат предыдущей.

    Args:
        *functions (Callable): Функции для композиции.

    Returns:
        Callable: Результирующая составная функция.

    Raises:
        TypeError: Если хотя бы один аргумент не является вызываемым объектом (callable).
    """
    if not functions:
        # Единичная функция (identity), если аргументы не переданы
        return lambda x: x

    for idx, fn in enumerate(functions):
        if not callable(fn):
            raise TypeError(f"Аргумент на позиции {idx} не является вызываемым объектом: {fn!r} ({type(fn).__name__}).")

    if len(functions) == 1:
        return functions[0]

    return reduce(
        lambda outer, inner: lambda *args, **kwargs: outer(inner(*args, **kwargs)),
        functions
    )


def pipe(*functions: Callable[..., Any]) -> Callable[..., Any]:
    """Создаёт конвейер функций (вычисление слева направо).

    Математическое определение: pipe(f, g, h)(x) = h(g(f(x))).
    Удобно для последовательного пайплайна обработки данных.

    Args:
        *functions (Callable): Функции для конвейера.

    Returns:
        Callable: Результирующая конвейерная функция.
    """
    return compose(*reversed(functions))


# Русскоязычные псевдонимы для совместимости
композиция = compose
конвейер = pipe
