first_number = int(input('Enter number a:'))
second_number = int(input('Enter number b:'))
print('list of possible operations:\na - addition\nb - subtraction')
print('c - division\nd - multiplication\ne - to the extent\nf - square root')
print('Select the operation number from the list:')
def addition(first_number,second_number):
    return first_number + second_number
def subtraction(first_number,second_number):
    return first_number - second_number
def division(first_number,second_number):
    return first_number / second_number
def multiplication(first_number,second_number):
    return first_number * second_number
def extent(first_number,second_number):
    return first_number ** second_number
def root(first_number,second_number):
    return first_number **(0.5)
a=addition(first_number,second_number)
b=subtraction(first_number,second_number)
c=division(first_number,second_number)
d=multiplication(first_number,second_number)
e=extent(first_number,second_number)
f=root(first_number,second_number)
