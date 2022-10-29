alphabet = ('abcdefghijklmnopqrstuvwxyz')
text = input('Enter text: ')
numbers = []
letters = []
twice = (0)
for i in  alphabet:
    once = 0
    for r in text:
        if i == r:
            once += 1
    if once > 0:
        #Adding letters and numbers to empty lists
        numbers.append(once)
        letters.append(i)
#merge and sort
x1, y1 = zip(*sorted(zip(numbers, letters)))       
f=len(numbers)
while twice < f:
    print(y1[twice],'-',x1[twice])
    twice += 1
