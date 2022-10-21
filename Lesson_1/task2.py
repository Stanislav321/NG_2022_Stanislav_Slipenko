while True:
    first_number = int(input('Enter number a:'))
    second_number = int(input('Enter number b:'))
    z = input('list of possible operations:\n1 - addition\n2 - subtraction\n'\
    '3 - division\n4 - multiplication\n5 - to the extent\n6 - square root\n'\
    'Select the operation number from the list:')
    if z == '1':
        print(first_number+second_number)
    elif z == '2':
        print(first_number-second_number)
    elif z == '3':
        print(first_number/second_number)
    elif z == '4':
        print(first_number*second_number)
    elif z == '5':
        print(first_number**second_number)
    elif z == '6':
        print(first_number**(0.5))
    else:
     print('Error enter operator correctly')
    
