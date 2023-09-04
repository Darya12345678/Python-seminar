# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

import os
import json
import csv
import pickle

def calculate_directory_size(directory):
    """
    Рекурсивно вычисляет размер директории с учетом всех вложенных файлов и поддиректорий.
    """
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    return total_size

def save_directory_structure(directory, output_folder):
    """
    Рекурсивно обходит указанную директорию и сохраняет структуру в JSON, CSV и Pickle файлы.
    :param directory: Начальная директория для обхода.
    :param output_folder: Папка, в которой будут сохранены файлы.
    """
    result = []

    for dirpath, dirnames, filenames in os.walk(directory):
        dir_info = {
            "path": dirpath,
            "type": "directory",
            "size": calculate_directory_size(dirpath)
        }
        result.append(dir_info)

        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            file_info = {
                "path": filepath,
                "type": "file",
                "size": os.path.getsize(filepath)
            }
            result.append(file_info)

    # Сохраняем результаты в JSON
    with open(os.path.join(output_folder, "directory_structure.json"), "w") as json_file:
        json.dump(result, json_file, indent=4)

    # Сохраняем результаты в CSV
    with open(os.path.join(output_folder, "directory_structure.csv"), "w", newline="") as csv_file:
        fieldnames = ["path", "type", "size"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(result)

    # Сохраняем результаты в Pickle
    with open(os.path.join(output_folder, "directory_structure.pkl"), "wb") as pickle_file:
        pickle.dump(result, pickle_file)

# Пример использования:
directory_to_scan = "/путь/к/каталогу"
output_folder = "/путь/к/папке/для/результатов"

save_directory_structure(directory_to_scan, output_folder)
