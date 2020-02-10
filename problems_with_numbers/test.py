""""" 
Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих.
Начиная с 1 и 2, первые 10 элементов будут:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
 Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
"""""
number = 0
index = 0
total = 0
fibonacci_series = [1, 2]
while 1:
    number = fibonacci_series[index] + fibonacci_series[index+1]
    if number > 4000000:
        break
    fibonacci_series.append(number)
    index += 1
index = 0
for index in range(len(fibonacci_series)):
    if fibonacci_series[index] % 2 == 0:
        total += fibonacci_series[index]
print(total)
