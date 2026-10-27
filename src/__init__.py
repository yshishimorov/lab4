"""
Пакет лабораторной работы №4.
Функциональное программирование на Python.
Вариант 1.
"""

from src.task1_squares_map import (
    calculate_squares,
    get_squares_map,
    вычислить_квадраты,
    квадраты_чисел,
)
from src.task2_sum_reduce import (
    sum_positive_reduce,
    sum_reduce,
    сумма_reduce,
    сумма_положительных_reduce,
)
from src.task3_fibonacci import (
    fibonacci_generator,
    fibonacci_up_to_value,
    get_fibonacci_list,
    генератор_фибоначчи,
    список_фибоначчи,
    числа_фибоначчи_до,
)
from src.task4_compose import (
    compose,
    pipe,
    композиция,
    конвейер,
)
from src.task5_file_filter import (
    collect_filtered_lines,
    filter_file_lines,
    grep_file,
    поиск_в_файле,
    собрать_отфильтрованные_строки,
    фильтр_файла,
)

__all__ = [
    # Задание 1 (Средняя сложность №1)
    "get_squares_map",
    "calculate_squares",
    "квадраты_чисел",
    "вычислить_квадраты",
    # Задание 2 (Средняя сложность №3)
    "sum_reduce",
    "sum_positive_reduce",
    "сумма_reduce",
    "сумма_положительных_reduce",
    # Задание 3 (Средняя сложность №5)
    "fibonacci_generator",
    "fibonacci_up_to_value",
    "get_fibonacci_list",
    "генератор_фибоначчи",
    "числа_фибоначчи_до",
    "список_фибоначчи",
    # Задание 4 (Повышенная сложность №1)
    "compose",
    "pipe",
    "композиция",
    "конвейер",
    # Задание 5 (Повышенная сложность №4)
    "filter_file_lines",
    "grep_file",
    "collect_filtered_lines",
    "фильтр_файла",
    "поиск_в_файле",
    "собрать_отфильтрованные_строки",
]
