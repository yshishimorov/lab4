"""
Тесты для задания повышенной сложности №4: Фильтрация файла через генератор.
"""

import os
import tempfile
import types
import unittest
from src.task5_file_filter import (
    collect_filtered_lines,
    filter_file_lines,
    grep_file,
    фильтр_файла,
)


class TestFileFilter(unittest.TestCase):
    """Набор тестов для потоковой фильтрации файлов через генераторы."""

    def setUp(self) -> None:
        """Создание временного тестового файла."""
        self.temp_file = tempfile.NamedTemporaryFile("w+", delete=False, encoding="utf-8")
        self.temp_file.write(
            "1. Apple\n"
            "2. Banana\n"
            "3. Cherry\n"
            "4. Avocado\n"
            "5. Apricot\n"
        )
        self.temp_file.close()

    def tearDown(self) -> None:
        """Удаление временного файла."""
        if os.path.exists(self.temp_file.name):
            os.remove(self.temp_file.name)

    def test_filter_returns_generator(self) -> None:
        """Проверка, что функция возвращает генератор."""
        gen = filter_file_lines(self.temp_file.name, lambda line: True)
        self.assertIsInstance(gen, types.GeneratorType)

    def test_filter_predicate(self) -> None:
        """Проверка фильтрации строк, начинающихся на 'A'."""
        starts_with_a = lambda line: "A" in line
        lines = list(filter_file_lines(self.temp_file.name, starts_with_a))
        expected = ["1. Apple", "4. Avocado", "5. Apricot"]
        self.assertEqual(lines, expected)

    def test_grep_file(self) -> None:
        """Проверка работы функции grep_file."""
        banana_lines = list(grep_file(self.temp_file.name, "banana"))
        self.assertEqual(banana_lines, ["2. Banana"])

        no_match = list(grep_file(self.temp_file.name, "Orange"))
        self.assertEqual(no_match, [])

    def test_collect_filtered_lines_with_limit(self) -> None:
        """Проверка сбора отфильтрованных строк с лимитом."""
        all_lines = collect_filtered_lines(self.temp_file.name, lambda l: True, limit=2)
        self.assertEqual(len(all_lines), 2)
        self.assertEqual(all_lines, ["1. Apple", "2. Banana"])

    def test_file_not_found(self) -> None:
        """Проверка исключения при отсутствии файла."""
        with self.assertRaises(FileNotFoundError):
            list(filter_file_lines("non_existent_file.txt", lambda l: True))

    def test_invalid_predicate(self) -> None:
        """Проверка валидации невызываемого предиката."""
        with self.assertRaises(TypeError):
            list(filter_file_lines(self.temp_file.name, "не_предикат"))  # type: ignore

    def test_alias(self) -> None:
        """Проверка русскоязычного псевдонима."""
        self.assertIs(фильтр_файла, filter_file_lines)


if __name__ == "__main__":
    unittest.main()
