calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(*,string:str)-> tuple:
    count_calls()
    return len(string), string.upper(), string.lower()

def is_contains(*,string:str, list_to_search:list)-> bool:
    count_calls()
    for i in list_to_search:
        if string.upper() == i.upper():
            return True
    return False


string_info(string="Hello World")
print(string_info(string="Hello World"))
list_ = ["world", "heLlo","WOrld", "Urban", "pYtHon"]
print(is_contains(string="Python", list_to_search=list_))

print(calls)



