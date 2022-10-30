wrote = int(input('Number for the pyramid: '))
list = []
while wrote>=1:
    list.append(wrote)
    wrote -= 1
while len(list):
    print(' '.join(map(str, list)))
    del(list[0])
