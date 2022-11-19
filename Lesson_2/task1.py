text = input('Enter text: ')
text = list(text)
text.sort()
copy_element  = 0
for elem in text:
    if elem == copy_element:
        continue
    copy_element  = elem
    print(elem,"-",text.count(elem))
