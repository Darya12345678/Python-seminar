#Напишите функцию для транспонирования матрицы. Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]

def transpose_matrix(matrix):
   
    # Используем генератор списка и функцию zip для транспонирования матрицы
    transposed_matrix = [list(row) for row in zip(*matrix)]

    return transposed_matrix


# Пример использования
matrix = [[1, 2, 3], [4, 5, 6]]
transposed = transpose_matrix(matrix)
print(transposed)


#Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление. Пример: rev_kwargs(res=1, reverse=[1, 2, 3]) -> {1: 'res', '[1, 2, 3]': 'reverse'}
def rev_kwargs(**kwargs):
    """
    Функция принимает только ключевые параметры и возвращает словарь,
    где ключ - значение переданного аргумента, а значение - имя аргумента.

    Args:
        **kwargs: Ключевые параметры.

    Returns:
        Словарь, где ключ - значение переданного аргумента, а значение - имя аргумента.

    """
    reversed_kwargs = {str(value): key for key, value in kwargs.items()}

    return reversed_kwargs


# Пример использования
result = rev_kwargs(res=1, reverse=[1, 2, 3])
print(result)



# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
#  Дополнительно сохраняйте все операции поступления и снятия средств в список.

import math

initial_amount = 0
current_amount = initial_amount
transactions = []


def deposit(amount):
    """
    Функция для пополнения счета.

    Args:
        amount: Сумма для пополнения.

    Returns:
        None.

    """
    global current_amount

    if amount % 50 != 0:
        print("Сумма пополнения должна быть кратна 50 у.е.")
        return

    if current_amount >= 5000000:
        amount -= amount * 0.1

    current_amount += amount
    transactions.append(("Пополнение", amount))


def withdraw(amount):
    """
    Функция для снятия денег со счета.

    Args:
        amount: Сумма для снятия.

    Returns:
        None.

    """
    global current_amount

    if amount % 50 != 0:
        print("Сумма снятия должна быть кратна 50 у.е.")
        return

    if current_amount >= 5000000:
        amount -= amount * 0.1

    if amount > current_amount:
        print("Недостаточно средств на счете")
        return

    fee = max(30, min(amount * 0.015, 600))
    current_amount -= amount + fee
    transactions.append(("Снятие", amount))


def display_balance():
    """
    Функция для вывода текущего баланса.

    Args:
        None.

    Returns:
        None.

    """
    global current_amount

    print(f"Текущий баланс: {current_amount} у.е.")


def atm_program():
    """
    Основная программа банкомата.

    Args:
        None.

    Returns:
        None.

    """
    while True:
        print("Доступные действия:")
        print("1. Пополнить счет")
        print("2. Снять деньги")
        print("3. Выйти")

        choice = input("Выберите действие (1, 2, 3): ")

        if choice == "1":
            amount = float(input("Введите сумму для пополнения: "))
            deposit(amount)
            display_balance()
        elif choice == "2":
            amount = float(input("Введите сумму для снятия: "))
            withdraw(amount)
            display_balance()
        elif choice == "3":
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите действие снова.")


# Запуск программы
atm_program()

