#Purpose of A Decorator:
#Function which takes another function as an argument and returns another function
#Decorate a function
import os


def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

hi_func=outer_function("Hi")
bye_func=outer_function("Bye")

hi_func()
bye_func()

del hi_func

# hi_func() #Error because the function is not defined or deleted

bye_func()

print("************************************************************************************************************************")

def hello(name="Jose"):
    print("The hello() function has been executed")

    def greet(): #Defining another function inside hello
        return "This is inside greet() function"

    # Calling the greet function inside hello function and printing the return value of the function greet() which is "This is inside greet()"
    # print(greet())
    def welcome():
        return "This is inside welcome() function"

    # Calling the welcome function inside hello function and printing the return value of the function greet() which is "This is inside greet()"
    # print(welcome())

    #Below is the concept used to return the function inside the main function
    if name=="Jose":
        return greet
    else:
        return welcome

    print("This is the end of hello function")

hello() #Calling the hello function

my_new_func=hello("Sam") #Calling the hello function with an argument and storing the returned function in my_new_func
print(my_new_func()) #Calling the returned function

print("************************************************************************************************************************")

#Definiing a function inside a function and returning that function
def cool():
    def super_cool():
        return "I am very cool"

    return super_cool

    # print(super_cool()) #Error because the function is not defined or deleted

some_func=cool()
print(some_func())

print("************************************************************************************************************************")

#Passing a function as an argument to another function
def hello1():
    return "Hi there"

def other(func):
    print("Hello")
    print(func())

# print(func) #Printing the function object

other(hello1)
print("************************************************************************************************************************")
def new_decorator(func):
    def wrap_func():
        print("Code would be executed before executing the original function")
        func()
        print("Code would be executed after executing the original function")

    return wrap_func

def func_needs_decorator():
    print("This function is in need of a decorator")

func_needs_decorator()

print("************************************************************************************************************************")

#Decorating the function
decorated_func=new_decorator(func_needs_decorator)

decorated_func()
print("************************************************************************************************************************")

print("Using the new decorator syntax")
@new_decorator
def func_needs_decorator1():
    print("This function is in need of a decorator")

func_needs_decorator1()
print("************************************************************************************************************************")

#Prints the system user name
print(os.name())