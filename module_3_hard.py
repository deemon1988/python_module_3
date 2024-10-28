data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    # (6, {'cube': 7, 'drum': 8}),
    # "Hello",
    # ((), [{(2, 'Urban', ('Urban2', 35))}])
]


dict_= {'cube': 7, 'drum': 8}
k=0
w=0
for d, v in dict_.items():
    k += len(d)
    w += v
summ = k + w


print(*data_structure)

def calculate_srtucture_sum(data_structure):

    if len(data_structure) > 0:
        for i in data_structure:
          if isinstance(i,list):
              return sum(i) + calculate_srtucture_sum(data_structure[1:])
          elif isinstance(i, dict):
              k = 0
              w = 0
              for d, v in i.items():
                  k += len(d)
                  w += v
              summ = k + w
              return summ+calculate_srtucture_sum(data_structure[1:])
    else:
         return sum(data_structure[:1])

summary = calculate_srtucture_sum(data_structure)

print(summary)



