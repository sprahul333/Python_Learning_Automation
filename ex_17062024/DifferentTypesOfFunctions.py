def say_world():  # No Return Type and No Arguments/Parameters
    '''
    This function prints "Hello World" to the console.
    '''
    print("Hello World")


say_world();


def say_hello_arg(name):  # No Return Type and with arguments
    print("Hello " + name + " -- Printing the name from the arguments")


say_hello_arg("World")
say_hello_arg("Rahul")
say_hello_arg("Python")

print("*********************************************************************************************")


def say_hello_default(name="Stranger"):  # No Return Type and with default arguments
    print("Hello " + name + " -- Printing the name with default arguments")


# If we do not pass any arguments, it will take the default value
say_hello_default()

# If we pass any arguments, it will take the desired value, and put it in the function
say_hello_default("New Place")

# If we pass any arguments, it will take the desired value, and put it in the function
say_hello_default(name="Rahul")

# If we do not pass any arguments, it will take the default value
say_hello_default()

print("*********************************************************************************************")


def sumOfTheNumbers(a, b):  # Return Type and with arguments
    return a + b


print(sumOfTheNumbers(4, 10))

# Passing the values along with the parameter name
print(sumOfTheNumbers(a=4, b=102))

print(sumOfTheNumbers(b=42, a=1022))


# Cannot run the below code because we have passed unexpected arguments, in this case we have the argument names as a,b
# print(sumOfTheNumbers(l=42,m=122))

print("*********************************************************************************************")

def f1(a, b, c):
    return a + b + c;
    print("Hello") #Any Block of Code after return statement will not be executed, it will not throw any error

result= f1(3,4,5)
print(result)

#Passing the arguments along with variable name can be rearranged in any order
result= f1(c=10,a=10,b=29)
print(result)

#Function needs to be defined first then only it can be called

# say_hello_default() #This will throw an error because the function is not defined yet
#
# def say_hello_default(name="Stranger"):  # No Return Type and with default arguments
#     print("Hello " + name + " -- Printing the name with default arguments")

print("*********************************************************************************************")

def sumOfTheNumbers(a=2, b=2, c=3):  # Return Type and with arguments
    return a + b+ c

print(sumOfTheNumbers())

#Takes the default value of c and takes the values of a, b from the arguments and prints the sum
print(sumOfTheNumbers(4, 10))
