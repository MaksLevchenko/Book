import json
from models import Book


# Добавление книги
def add_book() -> None:

    book_1 = input('Введите через пробел название, автора и год издания книги, которую хотите добавить: ').split()
    
    if len(book_1) == 3:

        with open('books.txt', 'r', encoding='utf-8') as file:
            data = json.load(file)

        title, author, year = book_1

        book = Book()

        if data['books']:
            book.id = data['books'][-1]['book_id'] + 1
        else:
            book.id = 1
        book.title = title
        book.author = author
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
            
        print(f'книга {book.title} успешно добавленна в базу с id {book.id}')
    else:
        print('Вы что-то неправильно ввели(')
        add_book()

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
        for book in data['books']:
            if book['book_title'] == search or book['book_author'] == search or book['book_year'] == search:
                print(book['book_title'])
                print(book['book_author'])
                print(book['book_year'])
                print(book['book_status'])
            else:
                print('К сожалению такой книги у нас нет(')
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

    if book_status == 'в наличии' or book_status == 'выдана':
        with open('books.txt', 'r', encoding='utf-8') as file:
            data = json.load(file)

        if data['books']:
            for book in data['books']:
                if book['book_id'] == int(book_id):
                    book['book_status'] = book_status
                    with open('books.txt', 'w', encoding='utf-8') as file:
                        json.dump(data, file)
                    print()
                    print(f'Статус книги с id {book_id} успешно изменён на {book_status}')
                    print()
                else:
                    print()
                    print(f'К сожалению книги с id {book_id} у нас нет(')
                    print()
