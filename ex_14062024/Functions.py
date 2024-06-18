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

