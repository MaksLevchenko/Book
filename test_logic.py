from logic import add_book
from new import sum
from models import BookManager

from unittest import TestCase
from unittest.mock import patch


class LogicTestCase(TestCase):

    def test_add_book(self):
        """Тест добавления книги в базу"""
        book = BookManager(id=0, title="Bww", author="Www. w. w.", year="1111")
        result = book.add_book()

        real = f"книга Bww успешно добавленна в базу с id 0"
        self.assertEqual(result, real)

    def test_search_book(self):
        """Тест поиска книги"""
        real = [
            {
                "book_id": 1,
                "book_title": "Aww",
                "book_author": "Www. w. w.",
                "book_year": "1111",
                "book_status": "в наличии",
            }
        ]
        book = BookManager(id=1, title="Aww", author="Www. w. w.", year="1111")
        book.add_book()
        result = BookManager.search_book("aww")
        self.assertEqual(result, real)

    def test_del_book(self):
        """Тест удаления книги из базы"""
        result = BookManager.del_book(0)
        self.assertEqual(result, True)

    def test_change_status_book(self):
        """Тест изменения статуса книги"""
        result = BookManager.change_status_book(0, "выдана")
        self.assertEqual(result, True)

    def test_search_book_bad(self):
        """Негативный тест поиска книги"""
        real = []
        result = BookManager.search_book("www")
        self.assertEqual(result, real)

    def test_del_book_bad(self):
        """Негативный тест удаления книги из базы. Тест срабатывает при неправильном id книги"""
        result = BookManager.del_book(-1)
        self.assertEqual(result, False)

    def test_change_status_book_bad(self):
        """Негативный тест изменения статуса книги. Тест срабатывает при неправильном id книги или неправильном статусе"""
        result = BookManager.change_status_book(-1, "невыдана")
        result_1 = BookManager.change_status_book(1, "выдана")
        result_2 = BookManager.change_status_book(1, "")
        self.assertEqual(result, False)
        self.assertEqual(result_1, False)
        self.assertEqual(result_2, False)

    def test_z_del(self):
        """Очищение книг добавленных в тестах"""
        result = BookManager.del_book(1)
        self.assertEqual(result, True)

    def test_sum(self):
        """Тест сложения двух чисел"""
        result = sum(2, 3)
        self.assertEqual(result, 6)
