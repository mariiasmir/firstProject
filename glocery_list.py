import json
print("Словарь <каталог продуктов>")
# открываем json файл (по умолчанию только чтений)
# сохраняем данные из файла в словарь product_list
with open('glocery_list.json') as data:
    product_list = json.load(data)
# load() - метод считывает файл в формате json
# и возвращает объекты Python
print(product_list)
"""""
# <Чтобы отсортировать словарь по ключам, надо создать список
из ключей словаря и далее произвести вывод списка и
словаря с помощью цикла>
product_list = list(product_catalog.keys())
product_list.sort()
for index in product_list:
   print(index, ':', product_catalog[index])
<Показать цену продукта>
print(product_catalog['milk'])
setdefault(key, default) - если key и default в словаре
нет, то они добавляются в словарь
"""""
