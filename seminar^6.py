import argparse        # модуль argparse, который позволяет управлять аргументами командной строки.

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

def main():
    parser = argparse.ArgumentParser(description="Проверяет дату на корректность.") # Создается объект ArgumentParser из модуля argparse. Этот объект позволяет определить, какие аргументы и параметры командной строки может принимать скрипт. Описание "Проверяет дату на корректность." используется для создания описания программы, которое будет отображаться при вызове скрипта с аргументом -h или --help.
    parser.add_argument("date", help="Дата в формате 'дд.мм.гггг' для проверки.")   # Добавляется аргумент date к парсеру. Это означает, что скрипт ожидает один обязательный аргумент при вызове из командной строки, который будет интерпретироваться как дата. Описание "Дата в формате 'дд.мм.гггг' для проверки." используется для вывода справки о том, как использовать этот аргумент, если пользователь вызывает скрипт с параметром -h или --help.
    args = parser.parse_args() # парсер анализирует аргументы командной строки, переданные при вызове скрипта, и сохраняет их в объект args. В данном случае, это ожидается, что будет передан один аргумент - дата.
    
    if check_date(args.date):                   # Если дата является корректной (функция check_date вернула True), то выводится сообщение о том, что дата корректна, и выводится сама корректная дата.
        print(f"Дата {args.date} корректна.")
    else:
        print(f"Дата {args.date} некорректна.")

if __name__ == "__main__":
    main()


# Чтобы запускать скрипт из командной строки, передавая дату в формате 'дд.мм.гггг':
# python скрипт.py 15.09.2023
# Скрипт выведет сообщение о том, корректна ли указанная дата или нет.