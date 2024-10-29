from bisect import insort
from reprlib import recursive_repr

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    #((), [{(2, 'Urban', ('Urban2', 35))}])
]


tuple_ = ((), [{(2, 'Urban', ('Urban2', 35))}])




def unpack_recursive(struc):
    if isinstance(struc, set):
        one_element = struc.pop()
    elif isinstance(struc, tuple|list):
        one_element = struc[:1]
    else:
        one_element = ()

    if  len(one_element) > 0 and isinstance(one_element, list|tuple|str|int):
        summ = 0
        for i in one_element:
            # while i <= len(one_element):
            if isinstance(i, int):
                summ += i
            elif isinstance(i, str):
                summ += len(i)
            elif isinstance(i,tuple|list|set) and len(i) > 0:
                return summ + unpack_recursive(i)
        else:
            return summ + unpack_recursive(struc[1:])
            # return unpack_recursive(i)

    else:
        return sum(struc[:1])

many_tuple = unpack_recursive(tuple_)
print(many_tuple)


def calculate_structure_sum(data_structure):
    if len(data_structure)>0:
        for i in (data_structure):
            if isinstance(i, str):
                str_=len(i)
                return str_ + calculate_structure_sum(data_structure[1:])
            if isinstance(i, tuple):
               # first = i[:1]
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
                        summ += k + w
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