import json
import os

from logic import add_book, del_book, search_book, view_books, change_status_book


# Главная функция программы
def main():
    print('Что Вы хотите сделать? Введите один из вариантов от 1 до 5: ')
    print(' 1 - Добавить книгу.')
    print(' 2 - Удалить книгу.')
    print(' 3 - Поиск книги.')
    print(' 4 - Все книги.')
    print(' 5 - Изменить статус книги.')

    action = input()
    
    if not action.isdigit() or int(action) <= 0 or int(action) > 5:
        print('Я Вас не понял:')
        main()
    else:
        if int(action) == 1:
            add_book()
        elif int(action) == 2:
            del_book()
        elif int(action) == 3:
            search_book()
        elif int(action) == 4:
            view_books()
        elif int(action) == 5:
            change_status_book()

# Создаём файл books.txt, если его ещё нет
if not os.path.exists('books.txt'):
    data = {}
    data['books'] = []
    with open('books.txt', 'a', encoding='utf-8') as file:
        json.dump(data, file)

if __name__ == "__main__":

    # Запускаем бесконечный цикл
    while True:
        # Вызываем функцию main
        main()