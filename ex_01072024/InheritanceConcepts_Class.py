class GrandParent:

    key="123@"
    def grandparent_method(self):
        return "Grandparent method"


#Inheritance Concept
class Parent(GrandParent):

    def parent_method(self):
        return "Parent method"


parent=Parent()

print(parent.parent_method())
print(parent.grandparent_method())
print(parent.key)

print("**********************************************************************************************************************")

class Father:

    def twoBHK(self):
        return "2BHK"


class Rahul(Father):

    def threeBHK(self):
        return "3BHK"

class Paluvai(Father):

    def fourBHK(self):
        return "4BHK"


class Lucky(Father):

    def noHome(self):
        return "No Home"


rahul=Rahul()

print(rahul.threeBHK());
print(rahul.twoBHK());

print("**********************************************************************************************************************")

#Mutiple Inheritance
#Diamond Problem is resolved by MRO -> Method Resolution Order

class A:
    def method1(self):
        print("A method1")

class B:
    def method2(self):
        print("B method2")


class C(A,B):
    def method3(self):
        print("C method3")


c = C()
c.method1()
c.method2()
c.method3()

print("**********************************************************************************************************************")

#Return Multiple Values

def multiple_return_values():
    a = 10
    b = 20
    c = 30
    return a, b, c

x, y, z = multiple_return_values()

print(x)  # Output: 10
print(y)  # Output: 20
print(z)  # Output: 30
print("**********************************************************************************************************************")

#Multi Level Inheritance:

class GF:
    def car(self):
        return "Old Car"

class F(GF):
    def car(self):
        return "Honda Civic"

class S(F):

    pass
    # def car(self):
    #     return "Lambo"


son=S()

print(son.car())