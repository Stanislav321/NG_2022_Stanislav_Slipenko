wrote = int(input('Number for the pyramid: '))
for elem in range(wrote):
    for secondelem in range(wrote - elem, 0, -1):
        print(secondelem, end=' ')
    print()
