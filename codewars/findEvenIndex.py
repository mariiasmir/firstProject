# Дан массив целых чисел.
# Ваша работа состоит в том, чтобы взять этот массив и найти индекс N,
# где сумма целых чисел слева от N равна сумме целых чисел справа от N.
# Если нет индекса, который бы это сделал, верните - 1.
new_array = [1, 2, 3, 4, 3, 2, 1]
new_array1 = [1, 100, 50, -51, 1, 1]


def find_even_index(arr):
    for index in range(len(arr)):
        if sum(arr[:index]) == sum(arr[index+1:]):
            return index
    else:
        return -1


print(find_even_index(new_array1))
