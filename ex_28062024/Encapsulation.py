#Encapsulation
#Bind the data variables with the methods

#that operate on these variables that is
#called encapsulation

#Data Member - Class Variables
#Methods - Def Function within the class

#Wrapping or binding the data variables with the methods
#Hide the data members by using only the methods

#Three Types of Access Modifiers
#public
#private - starts with __
#protected - starts with _
class Car:
    name="Name"
    __password = "XXXXXXXXXXX"

    def __init__(self):
        self.public_var="Public Variable"
        self._protected_var="Protected Variable"
        self.__private_var="Private Variable"
        print("Default Constructor")

    def __privateMethod(self):
        print("Private Method")

    def publicMethod(self):

        if(self.__private_var=="Private Variable"):
            print("Private Variable")
        print("Public Method")


xuv=Car()

#In a ideal scenario, no one should change the password outside of the class
#Password can be changed using the methods., no one should change the value outside of the class
xuv.password="345"
xuv.publicMethod()


print("********************************************************************************************************************************************")

class MyClass:

    def __init__(self):
        self.__name="Amit"

    def public_function(self):
        print("This is a public function")

    def __private_function(self):
        print("This is a private function")

    def public_fn_private(self):
        self.__private_function()
        print("This function is public but calls a private function")


#Creating an object of the class
obj=MyClass()

obj.public_function()
obj.public_fn_private()

print(obj.__name)

