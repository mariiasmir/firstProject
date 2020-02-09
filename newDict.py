# работает с текстовым файлом
glocery_list = {}
with open('newDict.txt', 'r') as new_dict:
    for line in new_dict:
        line = line.split()
        glocery_list[line[0]] = line[1]
# print(glocery_list)
glocery_list.setdefault('potato', '10')
# print(glocery_list)
del glocery_list['water']
# print(glocery_list)
print("\t<Словарь, считанный из файла>")
for key, value in glocery_list.items():
    print(f"{key:<7} : {value}")
