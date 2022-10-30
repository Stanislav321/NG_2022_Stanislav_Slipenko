list = input('List Entry: ')
splist = list.split(',')
no_copies = []
for i in splist:
    if i not in no_copies:
            no_copies.append(i)
print(no_copies)
