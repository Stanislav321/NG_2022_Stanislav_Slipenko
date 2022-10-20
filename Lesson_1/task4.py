print('Solve such a square equation: ax^2+bx+c=0')
a = int(input('Enter the first coefficient a:'))
b = int(input('Enter the second coefficient b:'))
c = int(input('Enter the loose member c:'))
koren = b*b-4*a*c
deskrem = koren**0.5
x1 = (-b+deskrem)/2*a
x2 = (-b-deskrem)/2*a
print(str(a)+'x^2+'+str(b)+'x+'+str(c)+'=0:','\nx1','=',x1, '\nx2','=',x2)
