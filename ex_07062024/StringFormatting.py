#First Way
print("This is my {} string".format("First"))

#Formatting the string based on the index position
print("This is my {1} string and {0} also".format("First","Second"))

#Formatting the string based on the variable names
print("This is my {q} string and {b} also".format(b="First", q="Second"))

print("***********************************************************************************************************************");

#Formatting the decimal numbers
result=100/777

#Format the decimal to 2 significant digits
print("The result is {r:1.2f}".format(r=result))

#Format the decimal to 5 significant digits
print("The result is {r:1.5f}".format(r=result))

#Format the decimal to 5 significant digits and adding more spaces before the decimal point to accomodate bigger values
print("The result is {r:10.5f}".format(r=result))

print("***********************************************************************************************************************");

#New Way of formatting names

#We are passing the variable name inside the curly braces
name="Rahul"
print(f'Hello, His name is {name}')

name="Sam"
age=4

print(f'Hello My name is {name} and my age is {age}')

