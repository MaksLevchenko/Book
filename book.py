# import json
# import os

# from logic import add_book, del_book, search_book, change_status_book
# from models import BookManager


# # Главная функция программы
# def main():
#     funk = {
#         '1': add_book,
#         '2': del_book,
#         '3': search_book,
#         '4': BookManager.view_books,
#         '5': change_status_book
#         }

#     # Вывод в консоль подсказки с доступными командами
#     print('Что Вы хотите сделать? Введите один из вариантов от 1 до 5: ')
#     print(' 1 - Добавить книгу.')
#     print(' 2 - Удалить книгу.')
#     print(' 3 - Поиск книги.')
#     print(' 4 - Все книги.')
#     print(' 5 - Изменить статус книги.')

#     # Ввод команды
#     action = input()

#     # Проверка на то, что команда является числом от 1 до 5
#     if action in funk:
#         funk[action]()
#     else:
#         print('Я Вас не понял:')
#         main()

# # Создаём файл books.txt, если его ещё нет
# if os.path.exists('books.txt'):
#     data = {}
#     data['books'] = []
#     with open('books.txt', 'r', encoding='utf-8') as file:
#         data_1 = file.readline()
#     if not data_1:
#         with open('books.txt', 'w', encoding='utf-8') as file:
#             json.dump(data, file)
# else:
#     data = {}
#     data['books'] = []
#     with open('books.txt', 'a', encoding='utf-8') as file:
#         json.dump(data, file)

# if __name__ == "__main__":

#     # Запускаем бесконечный цикл
#     while True:
#         # Вызываем функцию main
#         main()


import json
import os

from logic import add_book, del_book, search_book, change_status_book
from models import BookManager


# Функция для завершения программы
def exit_program():
    print("Завершение работы...")
    quit()


# Главная функция программы
def main():
    funk = {
        1: add_book,
        2: del_book,
        3: search_book,
        4: BookManager.view_books,
        5: change_status_book,
        6: exit_program,
    }

    # Вывод в консоль подсказки с доступными командами
    print("Что Вы хотите сделать? Введите один из вариантов от 1 до 6: ")
    print(" 1 - Добавить книгу.")
    print(" 2 - Удалить книгу.")
    print(" 3 - Поиск книги.")
    print(" 4 - Все книги.")
    print(" 5 - Изменить статус книги.")
    print(" 6 - Завершить программу.")

    # Ввод команды
    while True:
        action = input()
        if action.isdigit() and int(action) in funk:
            funk[int(action)]()
            break
        else:
            print("Неверная команда. Попробуйте снова.")


# Инициализация данных
if os.path.exists("books.txt"):
    data = {"books": []}
    with open("books.txt", "r+", encoding="utf-8") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            pass  # Файл пуст или повреждён, используем начальное значение data
else:
    data = {"books": []}
    with open("books.txt", "w", encoding="utf-8") as file:
        json.dump(data, file)


if __name__ == "__main__":
    # Запуск основной функции
    main()
