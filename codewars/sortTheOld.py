arr_1 = [5, 3, 2, 8, 1, 4]


def sort_array(source_array):
    if source_array == []:
        return source_array
    else:
        temp_arr = []
        for number in source_array:
            if number % 2 != 0:
                temp_arr.append(number)
        temp_arr = sorted(temp_arr)
        index_temp = 0
        for index in range(len(source_array)):
            if source_array[index] % 2 != 0:
                del source_array[index]
                source_array.insert(index, temp_arr[index_temp])
                index_temp += 1
            else:
                continue
        return source_array


print(sort_array(arr_1))
