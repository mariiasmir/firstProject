# Программа получает на вход слово и находит его середину
# Если слово четное - выводит дву буквы середины
# Если слова нечетное - выводит одну букву середины
new_str = 'testing'
new_str1 = 'middle'
new_str2 = 'A'


def get_middle(s):
    center = int(len(s) / 2)
    if len(s) % 2 == 0:
        return s[center-1:center+1]
    else:
        return s[center]


print(get_middle(new_str1))
