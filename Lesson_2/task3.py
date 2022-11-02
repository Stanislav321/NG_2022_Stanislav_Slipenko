wrote = int(input('Number for the pyramid: '))
for i in range(wrote):
    for r in range(wrote - i, 0, -1):
        print(r, end=' ')
    print()
