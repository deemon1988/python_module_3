def calculate_sum_and_length(data):
    total_sum = 0
    total_length = 0

    def recursive_calc(item):
        nonlocal total_sum, total_length

        if isinstance(item, int):  # Если элемент — число, добавляем к общей сумме
            total_sum += item
        elif isinstance(item, str):  # Если элемент — строка, добавляем длину к общей длине
            total_length += len(item)
        elif isinstance(item, (list, tuple, set)):  # Если элемент — список, кортеж или множество
            for sub_item in item:
                recursive_calc(sub_item)
        elif isinstance(item, dict):  # Если элемент — словарь
            for key, value in item.items():
                recursive_calc(key)  # Обрабатываем ключ
                recursive_calc(value)  # Обрабатываем значение

    recursive_calc(data)
    return total_sum, total_length


# Пример вызова функции
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_sum_and_length(data_structure)
print("Total sum of numbers:", result[0])
print("Total length of strings:", result[1])
