from logic import add_book
from new import sum
from models import Book

from unittest import TestCase
from unittest.mock import patch


class LogicTestCase(TestCase):

    def test_add_book(self):
        book = Book(id=1, title='Www', author='Www. w. w.', year='1111')
        result = book.add_book()

        real = f'книга Www успешно добавленна в базу с id 1'
        self.assertEqual(result, real)

    def test_del_book(self):
        result = Book.del_book(1)
        self.assertEqual(result, True)

    def test_search_book(self):
        real = [{"book_id": 1, "book_title": "Www", "book_author": "Www. w. w.", "book_year": "1111", "book_status": "в наличии"}]
        book = Book(id=1, title='Www', author='Www. w. w.', year='1111')
        book.add_book()
        result = Book.search_book('www')
        self.assertEqual(result, real)
