from itertools import count

# Tuples are similar to lists but they are immutable which means they cannot be changed
# List uses square brackets
# Dictionary uses curly braces
# Tupes uses parenthesis

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