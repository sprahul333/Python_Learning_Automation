class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Animal Constructor is called")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("Animal is eating")

cat=Animal("Cat", 5)

print(cat.name)
print(cat.age)

print("***************************************************************************************************")

#Inheritance in Python

#class Name(parentClass):
class Dog(Animal):

    def __init__(self, name, age):
        super().__init__(name, age)
        print("Dog Constructor is called")

    def who_am_i(self):
        print("I am a dog")
    def bark(self):
        print("Dog is barking")


dog1=Dog("Dog", 10)
print(dog1.name)
print(dog1.age)
dog1.eat()
dog1.who_am_i()