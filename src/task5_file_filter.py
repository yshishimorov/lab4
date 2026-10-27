"""
Лабораторная работа №4. Задание повышенной сложности №4.
Реализовать фильтрацию данных из файла через генератор.
"""

import os
from typing import Callable, Generator, List, Optional


def filter_file_lines(
    filepath: str,
    predicate: Callable[[str], bool],
    strip_newline: bool = True,
    encoding: str = "utf-8"
) -> Generator[str, None, None]:
    """Построчно фильтрует файл с использованием потокового генератора.

    Строки считываются лениво по одной, благодаря чему файл любого объёма
    обрабатывается за фиксированный объём памяти O(1).

    Args:
        filepath (str): Путь к файлу с данными.
        predicate (Callable[[str], bool]): Функция-предикат, возвращающая True для строк,
                                           которые должны быть включены в результат.
        strip_newline (bool): Удалять ли символ переноса строки в конце (по умолчанию True).
        encoding (str): Кодировка текстового файла (по умолчанию 'utf-8').

    Yields:
        str: Очередная строка файла, удовлетворяющая предикату.

    Raises:
        FileNotFoundError: Если указанный файл не найден.
        TypeError: Если predicate не является вызываемым объектом.
    """
    if not isinstance(filepath, str):
        raise TypeError("Путь к файлу должен быть строкой.")
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Файл не найден по пути: {filepath}")
    if not callable(predicate):
        raise TypeError(f"Предикат должен быть вызываемым объектом (callable), получено: {type(predicate).__name__}.")

    with open(filepath, "r", encoding=encoding) as file:
        for line in file:
            processed_line = line.rstrip("\r\n") if strip_newline else line
            if predicate(processed_line):
                yield processed_line


def grep_file(
    filepath: str,
    keyword: str,
    case_sensitive: bool = False,
    encoding: str = "utf-8"
) -> Generator[str, None, None]:
    """Удобный генератор-фильтр для поиска строк, содержащих ключевое слово (аналог утилиты grep).

    Args:
        filepath (str): Путь к файлу.
        keyword (str): Искомое ключевое слово или подстрока.
        case_sensitive (bool): Учитывать ли регистр символов (по умолчанию False).
        encoding (str): Кодировка файла.

    Yields:
        str: Строки, содержащие искомое ключевое слово.
    """
    if not isinstance(keyword, str) or not keyword:
        raise ValueError("Ключевое слово для поиска должно быть непустой строкой.")

    if case_sensitive:
        predicate = lambda line: keyword in line
    else:
        kw_lower = keyword.lower()
        predicate = lambda line: kw_lower in line.lower()

    return filter_file_lines(filepath, predicate=predicate, encoding=encoding)


def collect_filtered_lines(
    filepath: str,
    predicate: Callable[[str], bool],
    limit: Optional[int] = None
) -> List[str]:
    """Служебная функция для сбора отфильтрованных генератором строк в список.

    Args:
        filepath (str): Путь к файлу.
        predicate (Callable[[str], bool]): Функция фильтрации.
        limit (int, optional): Максимальное количество записей.

    Returns:
        List[str]: Список отобранных строк.
    """
    results = []
    for line in filter_file_lines(filepath, predicate):
        results.append(line)
        if limit is not None and len(results) >= limit:
            break
    return results


# Русскоязычные псевдонимы для совместимости
фильтр_файла = filter_file_lines
поиск_в_файле = grep_file
собрать_отфильтрованные_строки = collect_filtered_lines
