calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string:str)-> tuple:
    count_calls()
    return len(string), string.upper(), string.lower()

def is_contains(string, list_to_search)-> bool:
    count_calls()
    for i in list_to_search:
        print(i.upper())
        if string.upper() == i.upper():
            return True
        # else:
        #     continue
    return False


string_info("Hello World")
list_ = ["world", "heLlo","WOrld", "Urban", "python"]
print(is_contains("python", list_))


print(calls)



