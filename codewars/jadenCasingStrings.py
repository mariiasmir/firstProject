import string
str1 = "How can mirrors be real if our eyes aren't real"


def to_jaden_case(string):
    b = []
    for temp in string.split(' '): b.append(temp.capitalize())
    return ' '.join(b)


def to_Jaden_Case(string):
    return string.capwords(string)


print(to_Jaden_Case(str1))
