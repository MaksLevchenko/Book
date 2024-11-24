import json
from models import Book


# Добавление книги
def add_book() -> bool:
    """Функция предлагает ввод из консоли название, автора и год издания книги,
      и записывает книгу в файл books.txt в формате json присваивая книге id"""

    # Ввод названия и автора новой книги
    title = input('Введите название книги, которую хотите добавить: ')
    author = input('Введите автора книги, которую хотите добавить в формате Фамилия. И. О.: ')
    
    # Проверка на ввод автора
    if (len(author.split('.')) != 3 and len(author.split('.')[1].strip()) != 1 and len(author.split('.')[2].strip()) != 1)\
          or not (author.split('.')[0].strip().isalpha() and author.split('.')[1].strip().isalpha() and author.split('.')[2].strip().isalpha()):
        print()
        print('То что Вы ввели не похоже на автора книги в формате Фамилия. И. О.! Надо начинать сначала!')
        print()
        return add_book()

    # Ввод года издания новой книги
    year = input('Введите год издания книги, которую хотите добавить в формате ГГГГ: ')

    # Проверка на ввод года издания
    if len(year) != 4 and not year.isdigit():
        print()
        print('То что Вы ввели не похоже на год издания книги в формате ГГГГ.! Надо начинать сначала!')
        print()
        return add_book()

    title = title.capitalize()
    author = f"{author.split('.')[0].capitalize()}. {author.split('.')[1].strip().capitalize()}. {author.split('.')[2].strip().capitalize()}."
    year = year

    book = Book(title=title, author=author, year=year)

    print()
    print(book.add_book())
    print()
    
    return True

# Удаления книги по id
def del_book() -> None:
    """Функция предлагает ввод из консоли id книги, и удаляет книгу из файла books.txt"""

    # Ввод id
    book_id = input('Введите id книги, которую Вы хотите удалить: ')

    # Проверка id, на то, что введённые данные являются числом
    if book_id.isdigit():

        if not Book.del_book(int(book_id)):
            print()
            print(f'Книги с id {book_id} нет в нашем списке!')
            print()
            del_book()
    # Вывод ошибки, если введённое значение не является числом
    else:
        print()
        print('То, что Вы ввели не является числом!')
        print()
        del_book()

# Поиск книги по названию, автору или году издания книги
def search_book() -> None:
    """Функция предлагает ввод из консоли название, автора или год издания книги, и находит книгу в файле books.txt.
    Если поиск не увенчался успехом, то выводит соответствующее сообщение в консоль"""

    # Ввод названия, автора или года издания книги
    search = input('Введите название, автора или год издания книги: ').lower()
    books = Book.search_book(search=search)
    if books:
        print()
        for book in books:
            print(book['book_title'])
            print(book['book_author'])
            print(book['book_year'])
            print(book['book_status'])
            print()
    else:
        print()
        print('К сожалению такой книги у нас нет(')
        print()

# Изменение статуса книги
def change_status_book() -> None:
    """Функция предлагает ввод из консоли id книги и новый статус книги, и найдя книгу в файле books.txt меняет статус книги"""

    # Ввод id
    book_id = input('Введите id книги, которой нужно изменить статус: ')

    # Проверка id, на то, что введённые данные являются числом
    if not book_id.isdigit():
        print('То что Вы ввели не похоже на id!')
        change_status_book()

    # Ввод нового статуса книги
    book_status = input('Введите новый статус книги: ')

    # Проверка на то, что введённый статус соответствует стандартам
    if book_status.lower() == 'в наличии' or book_status.lower() == 'выдана':

        book = Book.change_status_book(int(book_id), book_status)
        if book:
            print()
            print(f'Статус книги с id {book_id} успешно изменён на {book_status}')
            print()
        else:
            print()
            print(f'К сожалению книги с id {book_id} у нас нет(')
            print()
    else:
        print('То что Вы ввели не похоже на статус!')
        change_status_book()
