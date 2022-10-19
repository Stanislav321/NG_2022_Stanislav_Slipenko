while True:
    a = int(input('Enter number a:'))
    b = int(input('Enter number b:'))
    z = input('list of possible operations:\n1 - addition\n2 - subtraction\n3 - division\n4 - multiplication\n5 - to the extent\n6 - square root \nSelect the operation number from the list:')

    if z == '1':
        print(a+b)

    elif z == '2':
        print(a-b)

    elif z == '3':
        print(a/b)

    elif z == '4':
        print(a*b)

    elif z == '5':
        print(a**b)

    elif z == '6':
        print(a**(0.5))

    else:
     print('Error enter operator correctly')
    
 
    

