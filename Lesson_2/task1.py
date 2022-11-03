alphabet = ('abcdefghijklmnopqrstuvwxyz')
text = input('Enter text: ')
for i in  alphabet:
    once = 0
    for r in text:
        if i == r:
            once += 1
    if once > 0:
        print(i,'-',once)
