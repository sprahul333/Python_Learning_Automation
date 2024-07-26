#Method Overriding

class Father:
    def home(self):
        print("I have a big house")


class Son(Father):
    def home(self):
        super().home() #Referring to the parent method present in the parent class
        print("I have a small house")
    # pass


son = Son()
son.home()

print("*********************************************************************************************************************************************")

#Method Overloading:

class MathUtils(object):

    # def add(self, a,b,c):
    #     return a+b+c

    def add(self, a,b=0,c=0):
        return a+b+c

    # def add(self,a,b):
    #     return a+b

math=MathUtils()

op1=math.add(3,4)
print(op1) #Output: 7

op2=math.add(3, 4, 5)
print(op2) #Output: 12

op3=math.add(3)
print(op3) #Output: 3

print("*********************************************************************************************************************************************")