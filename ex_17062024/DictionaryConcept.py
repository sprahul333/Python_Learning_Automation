# dictionaryOne=

#Dictionaries are unordered mappings for storing objects
#Allows users to quickly grab objects without needing to known the index position

#Objects retreived by key name and data cannot be sorted

my_dict={'key1':'value1','key2':'value2'}

print(my_dict)

#Printing the value based on the key
print(my_dict["key1"])

prices_lookup={'apples':2.99,'oranges':1.99,'milk':5.99,'bread':4.99,'meat':9.99,'eggs':6.99,'cheese':3.99}

print(prices_lookup['apples'])

#Having a dictonary having a list and another dictonary inside a key
d={'k1':123,'k2':[0,1,2],'k3':{'insideKey':100},'k4':["items","names","to","be","grabbed"]}

print(d['k2'])
print(d['k3']['insideKey'])

print(d['k4'][0].upper());

#Adding a new key to the dictionary
d['k5']=100

print(d)

#Replacing a value for that key in dictonary
d['k5']=200

print(d)

#Print the list of keys
print(d.keys());

#Prints the list of values
print(d.values());

#Prints the list of key value pairs
#Each Key value pair is a tuple
print(d.items())