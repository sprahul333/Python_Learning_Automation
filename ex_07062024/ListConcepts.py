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
list1.insert(2,10) #Inserting 10 at 2nd Index position

print(list1)

#Remove a value from the list
list1.remove(2)

print(list1)

list1= ["Hello","Doctor",432,33.32,'f',False]

print(list1)

#Data Type of list1 is List Class
print(type(list1))

print(list1[1:3])

#Adding Another List
#Same Like addAll function in JAVA
list1.extend(["Making","Engineers"])
print(list1)

#Prints the size of the list present
print(len(list1))

#Removes the last element and prints the index position of it
print(list1.pop())
print(list1)

print(list1[3])

#Reverse the complete list
list1.reverse()

print(list1)

#Sorting the data in ascending order
list1.sort()

print(list1)

#List is a mutuable sequence that means we can change the value at any index position
list1[2]=100

print(list1)