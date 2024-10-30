#  Задание "Раз, два, три, четыре, пять .... Это не всё?"

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(data_structure):
    summ = 0

    if len(data_structure) > 0:

        new_list = data_structure.copy()
        first = new_list[0]
        key, value = 0, 0

        for i in data_structure:

            if isinstance(i, dict):
                for k, v in i.items():
                    key += len(k)
                    value += v
                summ = key + value
                return summ + calculate_structure_sum(data_structure[1:])

            elif isinstance(i, set | list | tuple | str):
                for item in i:
                    if not item:
                        continue
                    elif isinstance(item, int):
                        summ += item
                    elif isinstance(item, str):
                        summ += len(item)
                    else:
                        new_list.remove(first)
                        new_list.insert(0, item)
                        if summ == 0:
                            calculate_structure_sum(new_list)
                        return summ + calculate_structure_sum(new_list)
                return summ + calculate_structure_sum(new_list[1:])
    else:
        return summ


result = calculate_structure_sum(data_structure)
print(result)
