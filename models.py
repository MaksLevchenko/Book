import json



# Модель книги
class Book():

    status: str = 'в наличии'

    def __init__(self, id: int, title: str, author: str, year: str):

        self.id = id
        self.title = title
        self.author = author
        self.year = year
        

    def del_book(id: int) -> bool:
        """Метод удаляет книгу из файла books.txt по id"""

        # Открытие файла books.txt
        with open('books.txt', 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Поиск книги по id и её удаление
        for book in data['books']:
            if book['book_id'] == id:
                data['books'].remove(book)
                with open('books.txt', 'w', encoding='utf-8') as file:
                    json.dump(data, file)
                print()
                print(f'Книга с id {id} успешно удалена.')
                print()
                return True
            # Вывод ошибки, если книги с таким id нет в базе
            else:
                return False
    
    def add_book(self) -> str:
        """Метод добавляет книгу в файл books.txt"""

        # Открытие файла books.txt
        with open('books.txt', 'r', encoding='utf-8') as file:
            data = json.load(file)

        data['books'].append({
        'book_id': self.id,
        'book_title': self.title,
        'book_author': self.author,
        'book_year': self.year,
        'book_status': 'в наличии'
        })
        
        # Запись новой книги в файл books.txt
        with open('books.txt', 'w', encoding='utf-8') as file:
            json.dump(data, file)

        return f'книга {self.title} успешно добавленна в базу с id {self.id}'
    
    def search_book(search: str) -> list:

        books = []

         # Открытие файла books.txt
        with open('books.txt', 'r', encoding='utf-8') as file:
            data = json.load(file)

        if data['books']:
            for book in data['books']:
                # Непосредственно поиск книги по названию, автору или году издания книги
                if book['book_title'].lower() == search or book['book_author'].lower() == search or book['book_year'] == search:
                    books.append(book)
        return books

    def change_status_book(id, status) -> bool:
        """Метод находит книгу по id в файле books.txt меняет статус книги"""

        # Открытие файла books.txt
        with open('books.txt', 'r', encoding='utf-8') as file:
            data = json.load(file)

        if data['books']:
            for book in data['books']:

                # Непосредственно изменение статуса книги
                if book['book_id'] == id:
                    book['book_status'] = status.lower()
                    with open('books.txt', 'w', encoding='utf-8') as file:
                        json.dump(data, file)
                    return True
                else:
                    False

    def view_books():
        """Метод выводит в консоль все книги"""

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

    