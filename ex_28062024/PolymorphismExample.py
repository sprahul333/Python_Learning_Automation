# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print("Dog Constructor is called")
#
#     def speak(self):
#         return self.name + " says Woof!"
#
#
# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print("Cat Constructor is called")
#
#     def speak(self):
#         return self.name + " says Meow!"
#
# niko=Dog("Niko",20);
# felix=Cat("Felix",20);
#
# print(niko.speak())
# print(felix.speak())
#
# for pet in [niko, felix]:
#     print(pet.speak())
#     print(type(pet))
#
# def pet_speak(pet):
#     print(pet.speak())
#
# print(type(pet))
#
# pet_speak(niko)
#

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self): #Abstract Method,Via Inheritance the logic should be implemented
        raise NotImplementedError("Subclass must implement abstract method")

# myanimal=Animal("Animal")

#Throws Error Because it is an abstract method and it should be called in the implemented class
# myanimal.speak()

class Dog(Animal):
    def speak(self):
        return self.name + " says Woof!"

fido=Dog("Fido")

print(fido.speak())
