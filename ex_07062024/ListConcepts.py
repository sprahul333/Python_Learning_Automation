#List - ordered collection of items
#Define a list of integers
# 1. Add a Item
# 2. Remove a Item
# 3. Update a item
# 4. View Item
# 5. Exit
list1 = [1, 2, 3]

print(list1)

#Arrays and List are same in Python
#Prints the number of values present in the list
print(len(list1))

print(list1[0])
print(list1[1])
print(list1[-1])

#Add a value to the list
list1.append(4)

print(list1)

#Remove a value from the list
list1.remove(2)

print(list1)