import json
from models import Book


# Добавление книги
def add_book() -> None:
    """Функция предлагает ввод из консоли название, автора и год издания книги,
      и записывает книгу в файл books.txt в формате json присваивая книге id"""

    # Ввод названия и автора новой книги
    title = input('Введите название книги, которую хотите добавить: ')
    author = input('Введите через пробел автора книги, которую хотите добавить в формате Фамилия. И. О.: ')

    # Проверка на ввод автора
    if (len(author.split('.')) != 3 and len(author.split('.')[1].strip()) != 1 and len(author.split('.')[2].strip()) != 1)\
          or not (author.split('.')[0].strip().isalpha() and author.split('.')[1].strip().isalpha() and author.split('.')[2].strip().isalpha()):
        print()
        print('То что Вы ввели не похоже на автора книги в формате Фамилия. И. О.! Надо начинать сначала!')
        print()
        add_book()

    # Ввод года издания новой книги
    year = input('Введите через пробел год издания книги, которую хотите добавить в формате ГГГГ: ')

    # Проверка на ввод года издания
    if len(year) != 4 and not year.isdigit():
        print()
        print('То что Вы ввели не похоже на год издания книги в формате ГГГГ.! Надо начинать сначала!')
        print()
        add_book()

    # Открытие файла books.txt
    with open('books.txt', 'r', encoding='utf-8') as file:
        data = json.load(file)

    book = Book()

    # Присвоение книги id
    if data['books']:
        book.id = data['books'][-1]['book_id'] + 1
    else:
        book.id = 1
    book.title = title.capitalize()
    book.author = f"{author.split('.')[0].capitalize()}. {author.split('.')[1].strip().capitalize()}. {author.split('.')[2].strip().capitalize()}."
    book.year = year

    data['books'].append({
        'book_id': book.id,
        'book_title': book.title,
        'book_author': book.author,
        'book_year': book.year,
        'book_status': 'в наличии'
        })
        
    # Запись новой книги в файл books.txt
    with open('books.txt', 'w', encoding='utf-8') as file:
        json.dump(data, file)
    print()
    print(f'книга {book.title} успешно добавленна в базу с id {book.id}')
    print()

# Удаления книги по id
def del_book() -> None:
    """Функция предлагает ввод из консоли id книги, и удаляет книгу из файла books.txt"""

    # Ввод id
    book_id = input('Введите id книги, которую Вы хотите удалить: ')

    # Проверка id, на то, что введённые данные являются числом
    if book_id.isdigit():

        # Открытие файла books.txt
        with open('books.txt', 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Поиск книги по id и её удаление
        for book in data['books']:
            if book['book_id'] == int(book_id):
                data['books'].remove(book)
                with open('books.txt', 'w', encoding='utf-8') as file:
                    json.dump(data, file)
                print(f'Книга с id {book_id} успешно удалена.')
            # Вывод ошибки, если книги с таким id нет в базе
            else:
                print(f'Книги с id {book_id} нет в нашем списке!')
                del_book()
    # Вывод ошибки, если введённое значение не является числом
    else:
        print('То, что Вы ввели не является числом!')
        del_book()

# Поиск книги по названию, автору или году издания книги
def search_book() -> None:
    """Функция предлагает ввод из консоли название, автора или год издания книги, и находит книгу в файле books.txt.
    Если поиск не увенчался успехом, то выводит соответствующее сообщение в консоль"""

    # Ввод названия, автора или года издания книги
    search = input('Введите название, автора или год издания книги: ')

    # Открытие файла books.txt
    with open('books.txt', 'r', encoding='utf-8') as file:
        data = json.load(file)

    if data['books']:
        print()
        for book in data['books']:
            # Непосредственно поиск книги по названию, автору или году издания книги
            if book['book_title'].lower() == search.lower() or book['book_author'].lower() == search.lower() or book['book_year'] == search:
                print(book['book_title'])
                print(book['book_author'])
                print(book['book_year'])
                print(book['book_status'])
            # Вывод ошибки, если книги с такими данными нет в базе
            else:
                print()
                print('К сожалению такой книги у нас нет(')
                print()
        print()
    # Вывод ошибки, если книги с такими данными нет в базе
    else:
        print('К сожалению такой книги у нас нет(')

# Вывод всех книг
def view_books() -> None:
    """Функция выводит в консоль все книги из файла books.txt"""

    # Открытие файла books.txt
    with open('books.txt', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Непосредственно вывод в консоль всех книг из базы
    if data['books']:
        print()
        print('Вот все наши книги:')
        print()
        for book in data['books']:
            print(book['book_title'])
            print(book['book_author'])
            print(book['book_year'])
            print(book['book_status'])
            print()
    # Вывод ошибки, если нет ни одной книги в базе
    else:
        print('К сожалению в данный момент у нас нет ни одной книги(')

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

        # Открытие файла books.txt
        with open('books.txt', 'r', encoding='utf-8') as file:
            data = json.load(file)

        if data['books']:
            for book in data['books']:

                # Непосредственно изменение статуса книги
                if book['book_id'] == int(book_id):
                    book['book_status'] = book_status.lower()
                    with open('books.txt', 'w', encoding='utf-8') as file:
                        json.dump(data, file)
                    print()
                    print(f'Статус книги с id {book_id} успешно изменён на {book_status}')
                    print()
                else:
                    print()
                    print(f'К сожалению книги с id {book_id} у нас нет(')
                    print()
