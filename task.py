data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(data_structure):
    *list_, = data_structure
    # first = list_[:1]
    key, value = 0, 0
    summ = 0
    if len(list_) > 0:
        for i in list_:
            if isinstance(i, int):
                summ += i
                return summ + calculate_structure_sum(list_[1:])
            elif isinstance(i, str):
                summ += len(i)
                return summ + calculate_structure_sum(list_[1:])
            elif isinstance(i, dict):
                for k, v in i.items():
                    key += len(k)
                    value += v
                summ = key + value
                return summ + calculate_structure_sum(list_[1:])
            elif isinstance(i, tuple | list | set):
                for j in i:
                    if not j:
                        continue
                    elif isinstance(j, int):
                        summ += j
                    elif isinstance(j, str):
                        summ += len(j)
                    elif isinstance(j, dict):
                        for k, v in j.items():
                            key += len(k)
                            value += v
                        summ = key + value
                    else:
                        return summ + calculate_structure_sum(j)
                return summ + calculate_structure_sum(list_[1:])
    else:
        return summ


res = calculate_structure_sum(data_structure)
print(res)
