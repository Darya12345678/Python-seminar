#Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов. [1, 2, 3, 1, 2, 4, 5] -> [1, 2]

def remove_duplicates(lst):
    """
    Функция удаляет дублирующиеся элементы из списка и возвращает список без дубликатов.

    Args:
        lst: Список с повторяющимися элементами.

    Returns:
        Список без дубликатов.

    """
    return list(set(lst))

# Пример использования
lst = [1, 2, 3, 1, 2, 4, 5]
result = remove_duplicates(lst)
print(result)



#В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.(Может помочь метод translate из модуля string)

import re
import string

def count_most_common_words(text, n=10):
    """
    Функция подсчитывает количество встречаемых слов в тексте и возвращает n самых часто встречающихся слов.

    Args:
        text: Текстовая строка.
        n: Количество самых часто встречающихся слов, которые нужно вернуть. По умолчанию 10.

    Returns:
        Список из n самых часто встречающихся слов.

    """
    # Преобразуем текст в нижний регистр
    text = text.lower()

    # Удаляем знаки препинания
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Используем регулярное выражение для разделения текста на слова
    words = re.findall(r"\b\w+\b", text)

    # Создаем словарь для подсчета встречаемости слов
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    # Сортируем словарь по значениям в убывающем порядке
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    # Возвращаем n самых часто встречающихся слов
    return [word for word, count in sorted_word_counts[:n]]


# Пример использования
text = """
Python is an interpreted high-level general-purpose programming language. 
Python's design philosophy emphasizes code readability with its 
notable use of significant indentation. Its language constructs as well as 
its object-oriented approach aim to help programmers write clear, 
logical code for small and large-scale projects.
"""

most_common_words = count_most_common_words(text)
print(most_common_words)

# В этом примере определена функция count_most_common_words, которая принимает текстовую строку и количество самых часто встречающихся слов, которые нужно вернуть (по умолчанию 10).
# Внутри функции выполнены следующие шаги:


# Преобразован текст в нижний регистр с помощью метода lower().

# Удаляены знаки препинания с помощью метода translate() и функции str.maketrans().

# Использовано регулярное выражение r"\b\w+\b" для разделения текста на отдельные слова с помощью функции re.findall().

# Создан словарь word_counts для подсчета встречаемости слов. Использован метод get() для получения значения слова из словаря и увеличиваем его на 1.

# Сортировка словаря word_counts по значениям в убывающем порядке с помощью функции sorted() и лямбда-функции key=lambda x: x[1].

# Возвращён список из n самых часто встречающихся слов, используя генератор списка и срез sorted_word_counts[:n].






# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.


def find_items_for_backpack(items, max_weight):
    """
    Функция находит вещи, которые помещаются в рюкзак с заданной грузоподъемностью.

    Args:
        items: Словарь со списком вещей и их массами в формате {вещь: масса}.
        max_weight: Максимальная грузоподъемность рюкзака.

    Returns:
        Все возможные варианты комплектации рюкзака в формате списка.

    """
    # Создаем матрицу для хранения максимальных масс вещей
    dp = [[0] * (max_weight + 1) for _ in range(len(items) + 1)]

    # Заполняем матрицу
    for i, (item, weight) in enumerate(items.items(), start=1):
        for w in range(1, max_weight + 1):
            if weight > w:
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(dp[i-1][w], weight + dp[i-1][w-weight])

    # Восстанавливаем выбранные вещи
    chosen_items = []
    i = len(items)
    w = max_weight
    while i > 0 and w > 0:
        if dp[i][w] != dp[i-1][w]:
            chosen_items.append(list(items.keys())[i-1])
            w -= list(items.values())[i-1]
        i -= 1

    # Возвращаем все возможные варианты комплектации рюкзака
    return chosen_items


# Пример использования
items = {
    'sleeping bag': 2,
    'tent': 5,
    'water bottle': 1,
    'food': 3,
    'flashlight': 1,
    'knife': 0.5
}
max_weight = 10

possible_combinations = find_items_for_backpack(items, max_weight)
print(possible_combinations)

