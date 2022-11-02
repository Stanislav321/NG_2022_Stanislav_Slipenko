wrote = input('List of numbers: ' )
str_list = wrote.split(sep=',')
str_list = list(map(int, str_list))
str_list.sort()
print(str_list[0])
print(str_list[-1])
del str_list[0]
del str_list[-1]
print(sum(str_list))
