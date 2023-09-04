import os

def rename_files(directory, desired_name, num_digits, source_extension, destination_extension, name_range=None):
    """
    Переименовать файлы в указанном каталоге с заданными параметрами.
    
    :param directory: Каталог, в котором нужно переименовать файлы.
    :param desired_name: Желаемое конечное имя файла (без порядкового номера).
    :param num_digits: Количество цифр в порядковом номере.
    :param source_extension: Расширение исходного файла.
    :param destination_extension: Расширение конечного файла.
    :param name_range: Диапазон сохраняемых символов из исходного имени (по умолчанию - None).
    """
    if not os.path.exists(directory):
        print(f"Каталог {directory} не существует.")
        return
    
    # Получить список файлов в указанном каталоге
    file_list = os.listdir(directory)
    
    # Фильтруем только файлы с заданным расширением
    filtered_files = [file for file in file_list if file.endswith(source_extension)]
    
    # Сортируем файлы, чтобы порядковый номер соответствовал порядку в списке
    filtered_files.sort()
    
    for index, file in enumerate(filtered_files, start=1):
        # Определяем новое имя файла
        new_name = desired_name
        if name_range:
            file_name = file[:-len(source_extension)]  # Убираем расширение
            if len(file_name) >= name_range[1]:
                file_name = file_name[name_range[0]:name_range[1]]
            new_name += file_name
        new_name += f"{index:0{num_digits}d}"  # Добавляем порядковый номер с ведущими нулями
        new_name += destination_extension
        
        # Полный путь к старому и новому файлу
        old_path = os.path.join(directory, file)
        new_path = os.path.join(directory, new_name)
        
        # Переименовываем файл
        os.rename(old_path, new_path)
        
        print(f"Переименован файл: {file} -> {new_name}")

# Пример использования:
directory = "путь_к_каталогу"
desired_name = "новое_имя_файла"
num_digits = 4
source_extension = ".jpg"
destination_extension = ".png"
name_range = (3, 6)

rename_files(directory, desired_name, num_digits, source_extension, destination_extension, name_range)
