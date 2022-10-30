wrote = int(input('The number for the factorial: '))
list = []
list2 = []
list3 = 1
while wrote>=1:
    list.append(wrote)
    wrote -= 1
for i in list:
    list3 = i*list3
    list2.append(list3)
print(list2[-1])

    
