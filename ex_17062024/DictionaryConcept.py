# dictionaryOne=
from collections import OrderedDict

# Dictionaries are unordered mappings for storing objects
# Allows users to quickly grab objects without needing to known the index position

# Objects retreived by key name and data cannot be sorted
#No Duplicate Keys but duplicate values are allowed

my_dict = {'key1': 'value1', 'key2': 'value2'}

print(my_dict)

# Printing the value based on the key
print(my_dict["key1"])

prices_lookup = {'apples': 2.99, 'oranges': 1.99, 'milk': 5.99, 'bread': 4.99, 'meat': 9.99, 'eggs': 6.99,
                 'cheese': 3.99}

print(str(len(prices_lookup))+"--- No Of Entries")
print(prices_lookup['apples'])
print(prices_lookup['oranges'])

# Having a dictonary having a list and another dictonary inside a key
d = {'k1': 123, 'k2': [0, 1, 2], 'k3': {'insideKey': 100}, 'k4': ["items", "names", "to", "be", "grabbed"]}

print(d['k2'])
print(d['k3']['insideKey'])

print(d['k4'][0].upper());

# Adding a new key to the dictionary
d['k5'] = 100

print(d)

# Replacing a value for that key in dictonary
d['k5'] = 200

print(d)

# Print the list of keys
print(d.keys());

# Prints the list of values
print(d.values());

# Prints the list of key value pairs
# Each Key value pair is a tuple
print(d.items())

print("**************************************************************************************************************")

# Unpacking a dictionary into another dictionary
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}


# In this example, `{**dict1, **dict2}` creates a new dictionary by unpacking the key-value pairs from `dict1` and `dict2`. If there are any duplicate keys, the last value for that key will be used in the resulting dictionary. [[3]](https://blog.finxter.com/python-double-asterisk/)
#
# Example with function calls:

def my_function(a, b, c):
    print(a, b, c)


my_dict = {'a': 1, 'b': 2}
my_function(**my_dict, c=3)  # Output: 1 2 3

print("**************************************************************************************************************")

#Another way of creating a dictionary
new_dict = dict(name="Rahul", age=25, city="Delhi")
print(new_dict)

print(new_dict["name"])

#If the value is present it will return the exact value
#Else it returns None
print(new_dict.get("Age"))


#Looping through a dictionary:

for k,v in new_dict.items():
    print(k,v)

#Ordered Dictionary ---> Preserves the order of insertion
od=OrderedDict()
od['a']=1
od['b']=2
od['c']=3

print(od)

for k,v in od.items():
    print(k,v)