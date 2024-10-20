def print_params(a = 1, b = 'строка', c = True):
    print(a)
    print(b)
    print(c)

values_list = [1, 'string', False]
values_dict = {'a':1,'b':(1,2,3),'c':True}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['string', 1]

print_params(*values_list_2,42)