import random

data_structure = [
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}]),
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
]

calls = 0

def count_calls():
    global calls
    calls += 1


def calc_stuct_sum(data_structure):
    count_calls()
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
                return summ + calc_stuct_sum(data_structure[1:])

            elif isinstance(i, set | list | tuple | str):
                for s in i:
                    if not s:
                        continue
                    elif isinstance(s, int):
                        summ += s
                    elif isinstance(s, str):
                        summ += len(s)
                    else:
                        new_list.remove(first)
                        new_list.insert(0, s)
                        if summ == 0:
                            calc_stuct_sum(new_list)
                        return summ + calc_stuct_sum(new_list)
                return summ + calc_stuct_sum(new_list[1:])
    else:
        return summ


random.shuffle(data_structure)
res = calc_stuct_sum(data_structure)
print(res)
print(calls)