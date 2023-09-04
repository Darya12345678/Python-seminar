#Создайте файл, в котором вы импортируете встроенные в модуль функции под псевдонимами. (3-7 строк импорта).

import math as m
import random as r
import datetime as dt
import os as o

# Использование функций с псевдонимами
print(m.sqrt(16))  # Используем функцию sqrt из модуля math с псевдонимом m
print(r.randint(1, 10))  # Используем функцию randint из модуля random с псевдонимом r
print(dt.date.today())  # Используем функцию today из модуля datetime с псевдонимом dt
print(o.getcwd())  # Используем функцию getcwd из модуля os с псевдонимом o


# Создайте модуль с функцией внутри. 
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток. 
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток. 
# Функция выводит подсказки “больше” и “меньше”. 
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

import random

def guess_number(lower_bound, upper_bound, attempts):
    random_number = random.randint(lower_bound, upper_bound)

    for _ in range(attempts):
        guess = int(input("Угадайте число: "))

        if guess == random_number:
            print("Поздравляю! Вы угадали число.")
            return True
        elif guess < random_number:
            print("Нет, загаданное число больше.")
        else:
            print("Нет, загаданное число меньше.")

    print("У вас закончились попытки. Загаданное число было", random_number)
    return False

# Улучшаем задачу 2. 
# Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала. 
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции. 
# Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.

import random
import sys

def guess_number(lower_bound, upper_bound, attempts):
    random_number = random.randint(lower_bound, upper_bound)

    for _ in range(attempts):
        guess = int(input("Угадайте число: "))

        if guess == random_number:
            print("Поздравляю! Вы угадали число.")
            return True
        elif guess < random_number:
            print("Нет, загаданное число больше.")
        else:
            print("Нет, загаданное число меньше.")

    print("У вас закончились попытки. Загаданное число было", random_number)
    return False

if __name__ == "__main__":
    args = sys.argv[1:]  # Получение аргументов командной строки, исключая имя самого скрипта

    if len(args) < 1 or len(args) > 3:
        print("Ошибка! Неверное количество аргументов.")
        print("Использование: python имя_скрипта.py [нижняя_граница] [верхняя_граница] [количество_попыток]")
    else:
        # Преобразование строковых аргументов командной строки в числовые параметры
        lower_bound = int(args[0])
        upper_bound = int(args[1]) if len(args) >= 2 else 100
        attempts = int(args[2]) if len(args) >= 3 else 10

        guess_number(lower_bound, upper_bound, attempts)


# Создайте модуль с функцией внутри. 
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны

def guess_riddle(riddle, options, attempts):
    for attempt in range(1, attempts+1):
        guess = input(f"Attempt {attempt}. Guess the riddle: ")
        if guess in options:
            print("Congratulations! You guessed the riddle.")
            return attempt
        else:
            print("Wrong guess. Try again.")
    print("Attempts exhausted. You couldn't guess the riddle.")
    return 0

# Добавьте в модуль с загадками функцию, которая хранит словарь списков. 
# Ключ словаря - загадка, значение - список с отгадками. 
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки. 

def add_riddles():
    while True:
        riddle = input("Enter a riddle (or 'q' to quit): ")
        if riddle == 'q':
            break
        options = input("Enter possible answers (separated by commas): ").split(',')
        riddles[riddle] = [option.strip() for option in options]

# Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число (номер попытки, с которой она угадана). 
# Функция формирует словарь с информацией о результатах отгадывания. 
# Для хранения используйте защищённый словарь уровня модуля.
# Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде. 
# Для формирования результатов используйте генераторное выражение.
def guess_riddle(riddle, options, attempts):
    for attempt in range(1, attempts+1):
        guess = input(f"Attempt {attempt}. Guess the riddle: ")
        if guess in options:
            print("Congratulations! You guessed the riddle.")
            _riddle_results[riddle] = attempt  # Записываем результат отгадывания в защищенный словарь
            return attempt
        else:
            print("Wrong guess. Try again.")
    print("Attempts exhausted. You couldn't guess the riddle.")
    _riddle_results[riddle] = 0  # Если не угадано, записываем 0 в защищенный словарь
    return 0


def get_guess_results():
    return _riddle_results


def display_results():
    results = [f"Riddle: '{riddle}', Attempts: {attempt}" for riddle, attempt in _riddle_results.items()]
    print("Guess Results:")
    print('\n'.join(results))

# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999]. 
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь. 
# Проверку года на високосность вынести в отдельную защищённую функцию.

def is_leap_year(year):
    """
    Проверяет, является ли год високосным.
    """
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def check_date(date_str):
    """
    Проверяет, может ли дата существовать.
    """
    try:
        day, month, year = map(int, date_str.split('.'))
        if year < 1 or year > 9999:
            return False
        if month < 1 or month > 12:
            return False
        if month in [1, 3, 5, 7, 8, 10, 12]:
            if day < 1 or day > 31:
                return False
        elif month in [4, 6, 9, 11]:
            if day < 1 or day > 30:
                return False
        elif month == 2:
            if is_leap_year(year):
                if day < 1 or day > 29:
                    return False
            else:
                if day < 1 or day > 28:
                    return False
        else:
            return False
        return True
    except ValueError:
        return False


#В модулях создайте дандер all и укажите только те функции, которые могут верно работать за пределами модуля.
__all__ = ['guess_number']