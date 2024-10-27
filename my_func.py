import string

str1 = 'Avery Breakwell abreakwell2@weather.com 850-192-9967'
f= open('example.txt','r')
#print(*f)
#tuple_ =[].append(*f.readlines())
#print(tuple_)
#print(*f.readlines())


def get_user_data(info: str) -> str:
    data = info.replace("\t", ' ')
    data_list = data.split(' ')
    u_email = mail(data_list)
    u_phone = phone(data_list)
    data_list.remove(u_email)
    data_list.remove(u_phone)
    u_name = ' '.join(data_list)
    u_phone = '('+u_phone[:3]+')' +u_phone[3:]
    #u_data = ', '.join([u_name,u_email,u_phone])
    u_data = f"'{u_name}', '{u_phone}', '{u_email}'"
    return f"({u_data})"



def mail(info: list) -> str:
    email = ''
    for str_ in info:
        if '@' in str_:
            email = str_
        elif str_.isdigit() and 1 < len(str_) < 15 and '-' not in str_:
            info.remove(str_)
    return email

def phone(info: list):
    is_phone = ''
    for i in info:
        if '-' in i:
            new_i = i.replace('-', '')
            if new_i.isdigit():
                is_phone = i
    return is_phone

def get_tuple(*values):
    list_ = []
    str_ = values[0]
    for i in values:
        list_.append(i)
    print(values)
    print(str_)
get_tuple(*f)


print("User data:",get_user_data(str1))



