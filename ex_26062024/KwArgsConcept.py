# ** dictionary with a variable argument
# * means var args in JAVA
def groceries( **itemsList):
    print(itemsList)
    for item in itemsList:
        print(itemsList[item])

groceries(item1="milk",item2="bread")

def myFunc(*args, **kwargs):
    print(args)
    print(kwargs)
    print("Total List of arguments are {} {}".format(args[0],kwargs['fruit']))

myFunc("apples", "oranges", "bananas", fruit="mangoes", veggie="potatoes")

print("******************************************************************************************************************************")


def myfunc(*args):
    sum = 0
    for i in args:
        sum+=i
    return sum

print(myfunc(1,2,3,4,5))

print(myfunc(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

print("******************************************************************************************************************************")


def myfunc(name):
    reversed_str = ""
    for i in name:
        if i.isupper():
           reversed_str+=i.lower()
        elif i.islower():
            reversed_str+=i.upper()
        else:
            reversed_str += i


    return reversed_str

print(myfunc("Hello World"))