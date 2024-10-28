#  Самостоятельная работа по уроку "Рекурсия"

def get_multiplied_digits(number:int):
    str_number = str(number).replace('0','')
    first = int(str_number[:1])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

print(get_multiplied_digits(40203))