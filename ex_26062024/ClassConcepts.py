# Class and Objects
# Class is a group of Objects which have some common properties
# Blueprint for creation of objects

# Class does not take much memory or negligible memory when created
# Objects consume memory in the heap whenever they are created

# Object is an instance of the class, all data members and member functions can be accessed with the help of class objects

class Person:

    # Attributes
    name=None
    age=None
    phone_number=None
    id=None

    # Behaviours
    def walk(self):
        print("I am walking")

    def another(self):
        print("Another method")

    def sleep(self,name):
        print(f"{name} is sleeping")

    def talk(self):
       return "Hello, I am talking"

    def eat(self,name):
        return f"{name} is eating"


#nothing happens if you execute the above program

#Syntax of creating an object
# reference=ClassName()

#Now we create an object of the person class
rahul=Person()

#Accessing the attributes of the object
rahul.name="Rahul"
print(rahul.name)

rahul.age=25
print(rahul.age)

rahul.phone_number=1234567890
print(rahul.phone_number)

rahul.id=1
print(rahul.id)

rahul.walk()

print("******************************************************************************************************************************")

class Dog:
    name=None

    def sleep(self):
        print("I am sleeping")

dog1=Dog()
dog1.name="Buddy"

print(dog1.name)

dog1.sleep()

print("******************************************************************************************************************************")

#Object is a run time entity

#Reference is a compile time entity

class Student:

    name = None
    age= None

    #Constructor is used to initialize the values of the instance variables

    #Self is a reference to the current instance of the class

    # __ means it is private in nature
    def __init__(self,name,age):
        self.name=name
        self.age=age

    # def __init__(self):
    #     print("Default Constructor")

    def talk(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old")

    def sleep(self):
        print(f"{self.name} is sleeping")

o1=Student("John", 30)

o1.talk()

print(f'{o1.name} has age {o1.age}')
print("******************************************************************************************************************************")

