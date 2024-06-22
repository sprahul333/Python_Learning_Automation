# Sets are unordered collections of unique elements
# Duplicates are not allowed here

# Declaring the set
my_set = set()

# ADDING THE values to the set
my_set.add(1)

print(my_set)

my_set.add(4);

my_set.add(2);
my_set.add(3);
my_set.add(4);

my_set.add(5);

my_set.add(6);

my_set.add(5);

print(my_set)

new_set = set();

new_set.add(10)
new_set.add(11)
new_set.add(12)
new_set.add(13)
new_set.add(14)
new_set.add(15)

new_set.add(16)
union_set=my_set.union(new_set)

print(union_set)

my_list=[1,1,2,4,5,235,6,23,6,-2,5,6]

#Converting the list to set
list_to_set=set(my_list)

print(list_to_set)

print("**********************************************************************************************")

set1=set(["a","b","c"])
set2=set(["a", "d", "e"])

set3=set(["a", "b", "c", "d", "e"])

#Checking the sub set concept
print(set1.issubset(set3))

#Checking the super set concept
print(set3.issuperset(set1))

print("**********************************************************************************************")

set4=set(["a", "b", "c"])
set5=set(["a", "d", "e"])

set6=set(["x", "y", "z"])
print(set4.isdisjoint(set5))

print(set4.isdisjoint(set6))

print("**********************************************************************************************")

set4=set(["a", "b", "c"])
set5=set(["a", "d", "e"])

#Finding the common values between two sets
my_set=set4.intersection(set5)
print(my_set)

print("**********************************************************************************************")

#Difference between two sets
set4=set(["a", "b", "c"])

set5=set(["a", "d", "e"])

print(set4.difference(set5))
print(set5.difference(set4))
print("**********************************************************************************************")

#using for loop to print the sets
print("Printing the sets using for loop")

for i in set4:
    print(i)

print("**********************************************************************************************")

#Removing the elements from the set
set4.remove('b')

print(set4)

