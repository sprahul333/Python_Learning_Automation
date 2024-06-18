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

