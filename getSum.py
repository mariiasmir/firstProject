# Программа получает на вход два числа и находит сумму всех чисел,
# находящихся между ними (включая сами числа)
f_num = 0
s_num = -1


def get_sum(a, b):
    new_sum = 0
    if a == b:
        return a
    else:
        if b < a:
            a, b = b, a
        for i in range(a, b+1):
            new_sum += i
    return new_sum


print(get_sum(f_num, s_num))
