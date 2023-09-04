# Напишите следующие функции:

# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

import csv
import json
import random
import math
from functools import wraps

# Функция для нахождения корней квадратного уравнения
def quadratic_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (root1, root2)
    elif discriminant == 0:
        root1 = -b / (2*a)
        return (root1,)
    else:
        return ()

# Функция для генерации CSV файла с тройками случайных чисел
def generate_csv(filename, num_rows):
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        for _ in range(num_rows):
            row = [random.uniform(1, 10) for _ in range(3)]
            csv_writer.writerow(row)

# Декоратор для запуска функции quadratic_roots с данными из CSV файла
def quadratic_roots_from_csv(csv_filename):
    def decorator(func):
        @wraps(func)
        def wrapper():
            with open(csv_filename, 'r') as csvfile:
                csv_reader = csv.reader(csvfile)
                results = []
                for row in csv_reader:
                    a, b, c = map(float, row)
                    roots = func(a, b, c)
                    results.append({'coefficients': (a, b, c), 'roots': roots})
                return results
        return wrapper
    return decorator

# Декоратор для сохранения параметров и результатов в JSON файл
def save_to_json(json_filename):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = func(*args, **kwargs)
            with open(json_filename, 'w') as jsonfile:
                json.dump(results, jsonfile, indent=4)
            return results
        return wrapper
    return decorator

# Пример использования декораторов:
csv_filename = 'random_numbers.csv'
generate_csv(csv_filename, 100)  # Генерируем CSV файл с 100 строками случайных чисел

@quadratic_roots_from_csv(csv_filename)
@save_to_json('results.json')
def find_quadratic_roots(a, b, c):
    return quadratic_roots(a, b, c)

results = find_quadratic_roots()  # Вызываем функцию, которая будет обернута декораторами
