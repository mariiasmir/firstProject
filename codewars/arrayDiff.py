# Ваша цель в этом ката - реализовать разностную функцию,
# которая вычитает один список из другого и возвращает результат.
arr1 = [1, 2]
arr2 = [1]


def array_diff(a, b):
    len_arr = len(b)
    for item in a:
        if item == b:
            a.remove(item)


print(array_diff(arr1, arr2))
