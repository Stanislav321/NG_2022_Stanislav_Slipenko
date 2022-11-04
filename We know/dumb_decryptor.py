alphabet  =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
cipher = int(input('Shift on: '))
inpute = input("text: ").upper()   
conclusion = ''   
for i in inpute:
    once  = alphabet .find(i)
    once2 = once  + cipher
    if i in alphabet :
        conclusion += alphabet [once2]
    else:
        conclusion += i
print (conclusion)
