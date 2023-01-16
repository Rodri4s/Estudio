myList = [76, 92.3, 'hello', True, 4, 76]

# Add 'apple' and 76 to the list
myList = myList + ["apple",76]

#Insert 'cat' at position 3
myList.insert(3,"cat")

#Insert 99 at the start of the list
myList.insert(0,99)

#Find index of word 'hello'
print("Index of word hello: ",myList.index("hello"))

#Count number of 76's in list
print("Numer of 76's: ",myList.count(76))

#Remove the first occurrence of 76 from list.
myList.remove(76)

#Remove True from list with pop and index
myList.pop(myList.index(True))
print(myList)