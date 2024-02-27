list1= ['apple', 'dog','ball', 'elephant','cat']

list2 = []
newlist = []
for x in list1:
    print (x)

for x in list1:  #list comprehension with removal of some items from the list
    if "a" in x:
        list2.append(x)
print(list2)

newlist = [x for x in range(10)]
nlist = [x.upper() for x in list1]
print(nlist)
nlist = ['hello' for x in list1 ]
print(nlist)
list1.sort()
print(list1)
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

thislist.sort(reverse = True)

print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.sort(key = str.lower) #here it converts the upper case into the lower case for sorting

print(thislist)

#make a copy of a list
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
newList = thislist.copy()
print(newList)

#to join any two lists.

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#or the another way is

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list1:
  list2.append(x)

print(list2)