class Dog:

    #CLASS OBJECT ATTRIBUTE

    species = "mammal"
    def __init__(self,breed,name, spots):
        self.breed = breed
        self.name = name

        #Expecting true or false
        self.spots = spots

     #ACTIONS
    def bark(self, number):
        print(f'"WOOF! My name is {self.name}" and the number is {number}')

#Parameterized Constructor ---> need to pass the variable during object creation
#If only parameterized constructor is there in the class, we have to mandatarily pass the arguments during the run time

my_dog = Dog("Labrador","Sammy",True)
print(type(my_dog))
print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)

print(my_dog.name)

print(my_dog.species)

my_dog.bark(300)


print("**********************************************************************************************************")

class Circle:
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius * radius * Circle.pi

    # def area(self):
    #     return self.area

    def circumference(self):
        return 2 * Circle.pi * self.radius
    def set_radius(self, new_radius):
        self.radius = new_radius

circle=Circle(20)

print(circle.circumference())
print(circle.area)
