import json
from models import Book


# Добавление книги
def add_book() -> None:

    title = input('Введите название книги, которую хотите добавить: ')
    author = input('Введите через пробел автора книги, которую хотите добавить в формате Фамилия. И. О.: ')
    if (len(author.split('.')) != 3 and len(author.split('.')[1].strip()) != 1 and len(author.split('.')[2].strip()) != 1)\
          or not (author.split('.')[0].strip().isalpha() and author.split('.')[1].strip().isalpha() and author.split('.')[2].strip().isalpha()):
        print()
        print('То что Вы ввели не похоже на автора книги в формате Фамилия. И. О.! Надо начинать сначала!')
        print()
        add_book()
    year = input('Введите через пробел год издания книги, которую хотите добавить в формате ГГГГ: ')
    if len(year) != 4 and not year.isdigit():
        print()
        print('То что Вы ввели не похоже на год издания книги в формате ГГГГ.! Надо начинать сначала!')
        print()
        add_book()

    with open('books.txt', 'r', encoding='utf-8') as file:
        data = json.load(file)

    book = Book()

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
        
    with open('books.txt', 'w', encoding='utf-8') as file:
        json.dump(data, file)
    print()
    print(f'книга {book.title} успешно добавленна в базу с id {book.id}')
    print()

# Удаления книги по id
def del_book() -> None:

    book_id = input('Введите id книги, которую Вы хотите удалить: ')

    if book_id.isdigit():

        with open('books.txt', 'r', encoding='utf-8') as file:
            data = json.load(file)

        for book in data['books']:
            if book['book_id'] == int(book_id):
                data['books'].remove(book)
                with open('books.txt', 'w', encoding='utf-8') as file:
                    json.dump(data, file)
                print(f'Книга с id {book_id} успешно удалена.')
            else:
                print(f'Книги с id {book_id} нет в нашем списке!')
                del_book()
    else:
        print('То, что Вы ввели не является числом!')
        del_book()

# Поиск книги по названию, автору или году издания книги
def search_book() -> None:

    search = input('Введите название, автора или год издания книги: ')

    with open('books.txt', 'r', encoding='utf-8') as file:
        data = json.load(file)

    if data['books']:
        print()
        for book in data['books']:
            if book['book_title'].lower() == search.lower() or book['book_author'].lower() == search.lower() or book['book_year'] == search:
                print(book['book_title'])
                print(book['book_author'])
                print(book['book_year'])
                print(book['book_status'])
            else:
                print()
                print('К сожалению такой книги у нас нет(')
                print()
        print()
    else:
        print('К сожалению такой книги у нас нет(')

# Вывод всех книг
def view_books() -> None:

    with open('books.txt', 'r', encoding='utf-8') as file:
        data = json.load(file)

    if data['books']:
        print('Вот все наши книги:')
        print()
        for book in data['books']:
            print(book['book_title'])
            print(book['book_author'])
            print(book['book_year'])
            print(book['book_status'])
            print()
    else:
        print('К сожалению в данный момент у нас нет ни одной книги(')

# Изменение статуса книги
def change_status_book() -> None:

    book_id = input('Введите id книги, которой нужно изменить статус: ')

    if not book_id.isdigit():
        print('То что Вы ввели не похоже на id!')
        change_status_book()

    book_status = input('Введите новый статус книги: ')

    if book_status.lower() == 'в наличии' or book_status.lower() == 'выдана':
        with open('books.txt', 'r', encoding='utf-8') as file:
            data = json.load(file)

        if data['books']:
            for book in data['books']:
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
