#Strings has some inbuilt functions

#Functions are used to repeat the tasks and use that concept as per the coding concepts

name="Amit Kumar"

print(type(name))
print(id(name)) #Memory Address where it is stored
#Prints the String in capital letter
print(name.upper())
#Prints the String in small letters
print(name.lower())

#Prints the String in Title Case
print(name.title())

#Prints the length of the string which starts from 1
print(len(name))
print(name.__len__()) #Both are same

#Changes to the first letter of the string to capital letter
print(name.capitalize())

#Prints the number of times the character 'a' is repeated
print(name.count('a'))

#Prints the index of the character 'm' in the string
print(name.index('m'))

#Prints the character that is present at the second index position
print(name[2])

#Throws String Index Out of Range because we have to take the index position that is less than the length of the string
#Not Greater than the string
# print(name[100])

#String is immutable in Python
#Means we cannot change the string once it is assigned
# name[2]='B' #Throws an error

#Slicing of the String
print(name[0:2]) #Prints the characters from 0 to 2

#Prints the character that is present at the last index position
#When we put negative values, it will read the string in reverse order
print(name[-1])

#None Means nothing
#None means not a empty value or zero or 0.0 or anything nor a default value
#None will be used for variable initializations
#None does not consume any memory in the heap
name=None
print(type(name))
print(name)

#No Mathmatical operations are allowed with None

#Empty String
#An Empty String does consume some memory in the heap
name=""
print(name)

#Null values are not present in Python