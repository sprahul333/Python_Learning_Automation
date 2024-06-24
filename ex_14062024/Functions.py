#Python is all about functions
#Functions are used to organize code into logical groups
#Functions are used to write the generic code in a method and used to call them

#In Python we have lot of built in functions

#Below is the syntax of us
def add_numbers(a, b): #Function Definition
    return a + b

print(add_numbers(10,20))

#Syntax to create a new Function:
#definition
#calling it

#defined
#Function name should not start with a number or special characters
#Function name should start with A-Z, a-z

def greet():
    print("Hello, How are you")

greet() #Calling the function
greet()
greet()

print("*********************************************************************************************")

def greetings():
    print("Hello");
    print("How are you?");
    print("I am fine");
    print("Thank you");

greetings()
greetings()

print("*********************************************************************************************")

#Arguments are used to pass some information to the function

def greet(name): #Name is a parameter or argument
    print(f"Hello {name}, How are you?")

greet("Spurti")
greet("Rahul")
greet(869)

print("*********************************************************************************************")

def allowed_to_enter_python_class(password):
    if(password == "123" or password == 123):
        print("You are allowed to enter")
    else:
        print("You are not allowed to enter")
        print("Please try again")

allowed_to_enter_python_class("123")
allowed_to_enter_python_class(123)


print("*********************************************************************************************")

def say_hello(name="Harry"):
    print(f"Hello {name}")

say_hello()

print("*********************************************************************************************")

def product_numbers(a, b):
    return a * b

product=product_numbers(10,20)
print(product)

print(type(product))

print("*********************************************************************************************")


def even_check(number):
    return number % 2 == 0

print(even_check(20))
print(even_check(21))

print("*********************************************************************************************")

#Checks for a list of numbers

even_numbers=[]
def check_even_list(num_list):
    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
            return True
        else:
            pass
    return False

print("For the list of numbers")
print(check_even_list([1,3,5,7,9,11,13,15,17,19,20]))

print(even_numbers)