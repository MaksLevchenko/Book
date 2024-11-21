import json



# Модель книги
class Book():
    id = int
    title = str
    author = str
    year = str
    status = 'в наличии'

    def del_book(self):
        """Метод удаляет книгу из файла books.txt по id"""

        # Открытие файла books.txt
        with open('books.txt', 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Поиск книги по id и её удаление
        for book in data['books']:
            if book['book_id'] == int(self.id):
                data['books'].remove(book)
                with open('books.txt', 'w', encoding='utf-8') as file:
                    json.dump(data, file)
                print(f'Книга с id {self.id} успешно удалена.')
                return True
            # Вывод ошибки, если книги с таким id нет в базе
            else:
                print(f'Книги с id {self.id} нет в нашем списке!')
                return False
    
    def add_book(self):
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
        print()
        print(f'книга {self.title} успешно добавленна в базу с id {self.id}')
        print()

    def change_status_book(self):
        """Метод находит книгу по id в файле books.txt меняет статус книги"""

        # Открытие файла books.txt
        with open('books.txt', 'r', encoding='utf-8') as file:
            data = json.load(file)

        if data['books']:
            for book in data['books']:

                # Непосредственно изменение статуса книги
                if book['book_id'] == int(self.id):
                    book['book_status'] = self.status.lower()
                    with open('books.txt', 'w', encoding='utf-8') as file:
                        json.dump(data, file)
                    print()
                    print(f'Статус книги с id {self.id} успешно изменён на {self.status}')
                    print()
                else:
                    print()
                    print(f'К сожалению книги с id {self.id} у нас нет(')
                    print()

    def view_books(self):
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

    