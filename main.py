"""
Лабораторная работа №4: Функциональное программирование на Python.
Вариант 1.

Студент: Шишиморов Ярослав Сергеевич
Группа: 221141
"""

import os
from src.task1_squares_map import get_squares_map
from src.task2_sum_reduce import sum_positive_reduce, sum_reduce
from src.task3_fibonacci import fibonacci_generator, get_fibonacci_list
from src.task4_compose import compose, pipe
from src.task5_file_filter import filter_file_lines, grep_file


def demo_task1() -> None:
    """Демонстрация задания 1 (Средняя сложность №1): Квадраты чисел с map."""
    print("=" * 70)
    print("ЗАДАНИЕ 1 (Средняя сложность №1): Вычисление квадратов чисел 1–10 с map")
    print("=" * 70)

    squares = get_squares_map(1, 10)
    print(f"Исходный диапазон: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
    print(f"Квадраты через map: {squares}")
    print()


def demo_task2() -> None:
    """Демонстрация задания 2 (Средняя сложность №3): Сумма чисел через reduce."""
    print("=" * 70)
    print("ЗАДАНИЕ 2 (Средняя сложность №3): Суммирование чисел с помощью reduce")
    print("=" * 70)

    sample_numbers = [10, 25, -5, 40, -15, 60]
    total_sum = sum_reduce(sample_numbers)
    positive_sum = sum_positive_reduce(sample_numbers)

    print(f"Исходный список чисел:            {sample_numbers}")
    print(f"Полная сумма (reduce):            {total_sum}")
    print(f"Сумма только положительных чисел: {positive_sum}")
    print()


def demo_task3() -> None:
    """Демонстрация задания 3 (Средняя сложность №5): Генератор Фибоначчи."""
    print("=" * 70)
    print("ЗАДАНИЕ 3 (Средняя сложность №5): Генератор чисел Фибоначчи (yield)")
    print("=" * 70)

    # Получение первых 12 чисел через генератор
    fib_list = get_fibonacci_list(12)
    print(f"Первые 12 чисел Фибоначчи: {fib_list}")

    # Демонстрация ленивой пошаговой генерации
    print("Пошаговое извлечение через next():")
    gen = fibonacci_generator()
    first_five = [next(gen) for _ in range(5)]
    print(f"  Первые 5 чисел из бесконечного генератора: {first_five}")
    print()


def demo_task4() -> None:
    """Демонстрация задания 4 (Повышенная сложность №1): Композиция функций (compose)."""
    print("=" * 70)
    print("ЗАДАНИЕ 4 (Повышенная сложность №1): Композиция функций (compose & pipe)")
    print("=" * 70)

    # 1. Математическая композиция: square(add_five(multiply_by_two(x)))
    # f(g(h(x))) -> compose(square, add_five, multiply_by_two)
    multiply_by_two = lambda x: x * 2
    add_five = lambda x: x + 5
    square = lambda x: x ** 2

    # При x = 3: (3 * 2) = 6 -> (6 + 5) = 11 -> (11 ^ 2) = 121
    composed_math = compose(square, add_five, multiply_by_two)
    print("1. Математическая цепочка: x -> (* 2) -> (+ 5) -> (^ 2)")
    print(f"   Результат compose(square, add_five, multiply_by_two)(3) = {composed_math(3)}")

    # 2. Строковый конвейер: pipe(strip -> lower -> replace)
    clean_text = pipe(
        lambda s: s.strip(),
        lambda s: s.lower(),
        lambda s: s.replace(" ", "_")
    )
    raw_str = "   ФУНКЦИОНАЛЬНОЕ ПРОГРАММИРОВАНИЕ НА PYTHON   "
    print(f"2. Конвейерная обработка текста:")
    print(f"   Исходная строка: '{raw_str}'")
    print(f"   Результат pipe:  '{clean_text(raw_str)}'")
    print()


def demo_task5() -> None:
    """Демонстрация задания 5 (Повышенная сложность №4): Фильтрация файла через генератор."""
    print("=" * 70)
    print("ЗАДАНИЕ 5 (Повышенная сложность №4): Фильтрация данных из файла через генератор")
    print("=" * 70)

    log_file = os.path.join(os.path.dirname(__file__), "data", "server_logs.txt")
    print(f"Чтение файла логов: {os.path.basename(log_file)}")

    # 1. Поиск критических ошибок через grep_file
    print("\nНайденные строки с ошибками (ERROR):")
    for error_line in grep_file(log_file, "ERROR"):
        print(f"  [!] {error_line}")

    # 2. Потоковая фильтрация предупреждений через произвольный предикат
    print("\nНайденные строки с предупреждениями (WARNING):")
    warning_gen = filter_file_lines(log_file, predicate=lambda line: "WARNING" in line)
    for warning_line in warning_gen:
        print(f"  [*] {warning_line}")
    print()


def main() -> None:
    """Точка входа демонстрационного приложения."""
    print("*" * 70)
    print(" МЕТОДЫ И ТЕХНОЛОГИИ ПРОГРАММИРОВАНИЯ (ЧАСТЬ 1)")
    print(" Лабораторная работа №4: Функциональное программирование на Python")
    print(" Студент: Шишиморов Ярослав Сергеевич | Группа: 221141 | Вариант: 1")
    print("*" * 70)
    print()

    demo_task1()
    demo_task2()
    demo_task3()
    demo_task4()
    demo_task5()

    print("=" * 70)
    print("Все задания варианта 1 лабораторной работы №4 успешно выполнены!")
    print("=" * 70)


if __name__ == "__main__":
    main()
