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
print('list of possible operations:\n1.addition\n2.subtraction')
print('3.division\n4.multiplication\n5.to the extent\n6.square root')
print('Select an operation from the list:')
addition = addition(first_number,second_number)
subtraction = subtraction(first_number,second_number)
division = division(first_number,second_number)
multiplication = multiplication(first_number,second_number)
extent = extent(first_number,second_number)
root = root(first_number,second_number)
