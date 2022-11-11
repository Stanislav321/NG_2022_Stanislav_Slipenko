def count(string):
    Object = {}
    for elem in string:
        if elem in Object:
            Object[elem] +=  1
        else:
            Object[elem]=1
    Object = dict(sorted(Object.items(), reverse = True, key=lambda x: x[1]))
    return Object
text = input('Enter text: ')
print(count(text))
