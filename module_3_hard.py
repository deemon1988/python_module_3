
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(data_structure):
    *list_, = data_structure
    first = list_[:1]
    key, value = 0, 0
    summ = 0
    for i in list_:
        if isinstance(i, str):
            summ = len(i)
            return summ + calculate_structure_sum(list_[1:])
        elif isinstance(i, int):
            summ += i
            return summ + calculate_structure_sum(list_[1:])
        elif isinstance(i, list):
            for j in i:
                if isinstance(j, int):
                   summ += j
                elif isinstance(j, str):
                    summ += len(j)
                elif isinstance(j, set):
                    for js in j:
                        return calculate_structure_sum(js)
            return summ + calculate_structure_sum(list_[1:])
        elif isinstance(i, dict):
            for k,v in i.items():
                key += len(k)
                value += v
            summ = key + value
            return summ + calculate_structure_sum(list_[1:])
        elif isinstance(i, tuple):
            for t in i:
                if isinstance(t, int):
                   summ += t
                elif isinstance(t, str):
                    summ += len(t)
                elif isinstance(t, dict):
                    for k1, v1 in t.items():
                        key += len(k1)
                        value += v1
                    summ += key + value
                else:
                    return calculate_structure_sum(i[1:])
            return summ + calculate_structure_sum(list_[1:])
    return sum(first)


result  = calculate_structure_sum(data_structure)
print(result)

