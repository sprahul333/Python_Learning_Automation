#Dynamically Typed Programming Language

jack=65
print(type(jack));
jack="Hello wrod"
print(type(jack));

#Different Data Types that Python supports
#variableName=variableValue
#identifier=literal

age=65;
isMale=True;
name="Rahul Paluvai"
pi=3.1424;
#age = variable name
# = assignment operator which helps in storing the value
# 65 = variable value

#Prints the data type of the age variable
print(type(age));
print(type(isMale));
print(type(name));
print(type(pi));

complex_number=2+3j
print(complex_number.real) #Prints the Real Number
print(complex_number.imag) #Prints the imaginary number

print("Todays Print Statement")
print(40-200)
print()

# self - Concept in OOPS which basically points to itself
# *args - Unlimited number of arguments (* - Unlimited Number of arguments like String, Float, Boolean, int etc)
# sep -' ' --> How you want to seperate the arguments
# end ='\n' - in the end what you want to do
# file= None - File IO

#Fix Indentation Errors do a right click and select reformat code
#Python is case sensitive
#By Default seperator is a single white space

print("Hello","world",43,6.34,True, sep='--');
print("Hi,My name is Rahul","Paluvai", sep="-");

#By Default end is a new line (\n)

print("Hi","Rahul","Paluvai", end="\t");
print("Hi","Rahul","Paluvai");

#Rules for Variable Names:
#Variable Names should start from A-Z and a-z
#Variable names should not start with a number, special character
#Variable names can have underscore
#Variable names cannot have any keywords
#Variable names should not be any space

#Snake_Case --> using underscore between the variable names and using small case
#Snake Case makes the python code more readable
first_name="Rahul"
last_name='Paluvai'
middle_name="""Raj""" #Multi Line String

print(type(last_name))
print(type(middle_name))