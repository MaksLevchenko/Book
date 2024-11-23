from logic import add_book
from new import sum
from models import Book

from unittest import TestCase
from unittest.mock import patch


class LogicTestCase(TestCase):

    def test_add_book(self):
        """Тест добавления книги в базу"""
        book = Book(id=0, title='Www', author='Www. w. w.', year='1111')
        result = book.add_book()

        real = f'книга Www успешно добавленна в базу с id 0'
        self.assertEqual(result, real)

    def test_search_book(self):
        """Тест поиска книги"""
        real = [{"book_id": 1, "book_title": "Aww", "book_author": "Www. w. w.", "book_year": "1111", "book_status": "в наличии"}]
        book = Book(id=1, title='Aww', author='Www. w. w.', year='1111')
        book.add_book()
        result = Book.search_book('aww')
        self.assertEqual(result, real)

    def test_del_book(self):
        """Тест удаления книги из базы"""
        result = Book.del_book(0)
        self.assertEqual(result, True)

    def test_change_status_book(self):
        """Тест изменения статуса книги"""
        result = Book.change_status_book(0, 'выдана')
        self.assertEqual(result, True)

    def test_z_del(self):
        """Очищение книг добавленных в тестах"""
        result = Book.del_book(1)
        self.assertEqual(result, True)
