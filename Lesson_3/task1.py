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
first_number = int(input('Enter number a:'))
second_number = int(input('Enter number b:'))
print('list of possible operations:\na - addition\ns - subtraction')
print('d - division\nm - multiplication\nt - to the extent\ns - square root')
print('Select an operation from the list:')
a = addition(first_number,second_number)
s = subtraction(first_number,second_number)
d = division(first_number,second_number)
m = multiplication(first_number,second_number)
t = extent(first_number,second_number)
s = root(first_number,second_number)
