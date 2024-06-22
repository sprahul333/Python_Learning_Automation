from itertools import count

# Tuples are similar to lists but they are immutable which means they cannot be changed
# List uses square brackets
# Dictionary uses curly braces
# Tuples uses parenthesis

tup = (1, 2, 3, 4, 5)

print(type(tup))
print(tup)

print(tup[2])

print(len(tup))

print(max(tup))

print(min(tup))

print(tup)

tup = (5, 2, -20, 4, 1, 20)

sorted_tup = sorted(tup)
print(sorted_tup)

# Prints the total number of elements present with value '2' in the tuple
print(sorted_tup.count(2))

#Prints the index position of the first occurence of the value '2'
print(sorted_tup.index(2))

#Clears the complete tuple
sorted_tup.clear()

print(sorted_tup)

print("***************************************************************************************************************************************************")

#Convert List to Tuple
list1 = [1, 2, 3, 4, 5]

tup1 = tuple(list1)
print(type(tup1))
print(tup1)
print("***************************************************************************************************************************************************")

#Deleting a Tuple
tup2 = (1, 2, 3, 4, 5)
print(tup2)
del tup2
print("***************************************************************************************************************************************************")

#Joining Two Tuples
tup3 = (1, 2, 3, 4, 5)
tup4 = ('a', 'b', 'c', 'd', 'e')

#Combining two tuples and storing them
tup5 = (tup3,tup4)

print(tup5)

print(tup5[0])
print(tup5[1])

#Prints the tuple that is present at 2nd index position in the first tuple
print(tup5[0][2])
print("***************************************************************************************************************************************************")