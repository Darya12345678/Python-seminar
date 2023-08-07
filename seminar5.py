#Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. 
#Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


import os

def split_path(filepath):
    path, filename = os.path.split(filepath)
    filename, ext = os.path.splitext(filename)
    return path, filename, ext

#Пример использования:

filepath = '/path/to/file.txt'
path, filename, ext = split_path(filepath)
print(path)  # '/path/to'
print(filename)  # 'file'
print(ext)  # '.txt'


#Напишите однострочный генератор словаря, который принимает на вход 
# три списка одинаковой длины: имена str, ставка int, премия str с указанием процентов вида «10.25%». 
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. 
# Сумма рассчитывается как ставка умноженная на процент премии


names = ['Alice', 'Bob', 'Charlie']
rates = [100, 200, 300]
bonuses = ['10.25%', '5%', '15%']

result = {name: rate * (float(bonus.strip('%')) / 100) for name, rate, bonus in zip(names, rates, bonuses)}

#Пример использования:

print(result)  # {'Alice': 10.25, 'Bob': 10.0, 'Charlie': 45.0}


#Создайте функцию генератор чисел Фибоначчи (см. Википедию)

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

#Пример использования:

fib_gen = fibonacci_generator()
for _ in range(10):
    print(next(fib_gen))

#Это простой генератор, который будет генерировать числа Фибоначчи на каждом вызове next(). 
# В примере это первые 10 чисел Фибоначчи.