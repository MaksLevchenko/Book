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
    action = int(input())
    if action == 1:
        add_book()
    elif action == 2:
        del_book()
    elif action == 3:
        search_book()
    elif action == 4:
        view_books()
    elif action == 5:
        change_status_book()
    else:
        print('Я Вас не понял:')
        main()

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