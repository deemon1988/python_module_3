

data_structure = [
    # [1, 2, 3],
    # {'a': 4, 'b': 5},
    # (6, {'cube': 7, 'drum': 8}),
    # "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

tuple_ = ((), [{(2, 'Urban', ('Urban2', 35))}])

print(*tuple_)

summ = 0
list_tuple = [*tuple_]
for j in tuple_:
    if isinstance(j,int):
        summ +=j
    elif isinstance(j,dict):
        k = 0
        w = 0
        #summ = 0
        for d, v in j.items():
            k += len(d)
            w += v
        summ = k + w


def calculate_structure_sum(data_structure):
    if len(data_structure)>0:
        for i in (data_structure):
            if isinstance(i, str):
                str_=len(i)
                return str_ + calculate_structure_sum(data_structure[1:])
            if isinstance(i, tuple):
                summ = 0
                for j in i:
                    if isinstance(j, int):
                        summ += j
                    elif isinstance(j, dict):
                        k = 0
                        w = 0
                        for d, v in j.items():
                            k += len(d)
                            w += v
                        summ = k + w
                return summ + calculate_structure_sum(data_structure[1:])
            elif isinstance(i, dict):
                k=0
                w=0
                summ= 0
                for d,v in i.items():
                    k += len(d)
                    w += v
                summ = k + w
                return summ + calculate_structure_sum(data_structure[1:])
            elif isinstance(i, list):

                return sum(i) + calculate_structure_sum(data_structure[1:])
    else:
        return sum(data_structure[:1])

count_sum = calculate_structure_sum(data_structure)
print(count_sum)