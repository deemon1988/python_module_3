#  Самостоятельная работа по уроку "Произвольное число параметров"

def single_root_words(root_word="Hello", *other_words) -> list:
    same_words = []
    for i in other_words:
        i = str(i)
        if root_word.upper() in i.upper():
            same_words.append(i)
        elif i.upper() in root_word.upper():
            same_words.append(i)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
