while True:
    first_number = int(input('Enter number a:'))
    second_number = int(input('Enter number b:'))
    print('list of possible operations:\n1 - addition\n2 - subtraction')
    print('3 - division\n4 - multiplication\n5 - to the extent\n6 - square root')
    operation = input('Select the operation number from the list:')
    if operation == '1':
        print(first_number+second_number)
    elif operation == '2':
        print(first_number-second_number)
    elif operation == '3':
        print(first_number/second_number)
    elif operation == '4':
        print(first_number*second_number)
    elif operation == '5':
        print(first_number**second_number)
    elif operation == '6':
        print(first_number**(0.5))
    else:
     print('Error enter operator correctly')
    
