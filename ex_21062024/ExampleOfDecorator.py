import time

#Decorators are so powerful and often use in frameworks as well.
#Promotes Code Reusability
#Enhanced Readability
#Seperation of Concerns

#Decorators can be used during logging, access control, memorization, timing
#There are several built in decorators in Python, such as @property, @staticmethod, and @classmethod.

def note_time_decorator(func):
    def wrapper():
        startTime= time.time()
        print("Start")
        func()
        print("End")
        endTime = time.time()
        print(f'Total time {endTime - startTime}')
    return wrapper()

@note_time_decorator
def logs_function():
    time.sleep(5)
    print("Prints the logs of the time taken")

@note_time_decorator
def report_logs():
    time.sleep(2)
    print("Prints the report of the logs")

print("**********************************************************************************************************************************")

#Adding Multiple Decorators:

def decorator(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper

def decorator_one(func):
    def wrapper():
        print("Start One")
        func()
        print("End One")
    return wrapper

@decorator
@decorator_one
def logs_function():
    time.sleep(5)
    print("Prints the logs of the time taken")

# logs_function()

print("**********************************************************************************************************************************")

#Built in decorators:

#property
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    name = property(get_name, set_name)
    age = property(get_age, set_age)

person = Person('John', 30)
print(person.name)  # Output: John
person.name = 'Jane'
print(person.name)  # Output: Jane
print(person.age)   # Output: 30
person.age = 31
print(person.age)   # Output: 31

print("**********************************************************************************************************************************")

#Static Method
class MyClass:
    @staticmethod
    def my_static_method():
        print("This is a static method.")

MyClass.my_static_method()  # Output: This is a static method.


print("**********************************************************************************************************************************")
#Class Method
class MyClass:
    @classmethod
    def my_class_method(cls):
        print(f"This is a class method. The class is {cls.__name__}.")
        # print(cls.__name__)

    def my_instance_method(self):
        print("This is an instance method.")


MyClass.my_class_method()
# Output: This is a class method. The class is MyClass.

obj = MyClass()

