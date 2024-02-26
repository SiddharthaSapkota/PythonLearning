print("hello world!!")


# To Create any list.

myList1 = ['apple', 'banana', 'orrange' ] 

myList2 = [1, 2 ,3, 4]

myList3 = ['true', 'false', 'true', 'true']

print(myList1, '\n')
print(myList2, '\n')
print(myList3, '\n')

print(len(myList1))
print(len(myList2))
print(len(myList3))


print(type(myList1))
print(type(myList2))
print(type(myList3))


thislist = list (('abc', 'def', 'ght'))
if 'abc' in thislist:
    print('"abc" is on the list.')
print('hello') 


thislist = list (('abc', 'def', 'ght'))
thislist[2] = 'thg'


print(thislist.insert(1,'klm'))
print(thislist)

print(thislist.append('qwe'))
print(thislist)


FirstList = ['qwe' , 'wer', 'ert']
SecondList =['rty', 'tyu' ,'yui']
FirstList.extend(SecondList) #extent is use to add the list items in to list from the right
print(FirstList)

FirstList.remove('rty')
print(FirstList)
FirstList.append('wer')
print(FirstList)
FirstList.remove('wer')
print(FirstList)
FirstList.pop(2)
print(FirstList)
FirstList.clear()
print(FirstList)


