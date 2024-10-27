import string

str1 = 'Avery Breakwell abreakwell2@weather.com 850-192-9967'
f= open('example.txt','r')

def get_user_data(*info: str) -> list:
    r_list = []
    for i in info:
        data = i.replace("\t", ' ')
        data = data.replace("\n", '')
        data_list = data.split(' ')
        u_email = mail(data_list)
        u_phone = phone(data_list)
        data_list.remove(u_email)
        data_list.remove(u_phone)
        u_name = ' '.join(data_list)
        u_phone = '('+u_phone[:3]+')' +u_phone[3:]
        u_data = f"'{u_name}', '{u_phone}', '{u_email}'"

        r_list.append(f"({u_data})")
    return r_list



def mail(info: list) -> str:
    email = ''
    for str_ in info:
        if '@' in str_:
            email = str_
        elif str_.isdigit() and 0 < len(str_) < 15 and '-' not in str_:
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

print("User data:",get_user_data(*f,))
f.close()

f= open('example.txt','r')
list_for_write = get_user_data(*f,)
f.close()

with open('output.txt','w') as f_out:
    for line in list_for_write:
        f_out.write(f"{line},\n")

f_out.close()





