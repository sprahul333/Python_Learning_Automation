#Function Scope
def func():
    x = 1 #Local Variables
    print(x) # 1
    print("Hello")

#Cannot use the variables declared inside the method, only global variables are allowed
# print(x)

func()

global_a=20 #Declared outside the functions

def func():
    # global a
    # a=10
    print(global_a)

func()
print(global_a)

#Having nested functions
def outer_function():
    var1=30
    def inner_function():
        global var2
        var2=40
        print("Inner function:",var1,var2)

    inner_function() #Invoking the inner function method inside a outer method

#Inner functions can access global variables and variables declared in the outer functions
#Calling a function
outer_function()

#We cannot call the functions inside the outer_function
# inner_function() #NameError: name 'inner_function' is not defined

# print("Outer function:", var1, var2)

print("*************************************************************************************************************************************")

list=[1,2,3]

def modifyList(list):
    list.append(200) #Modifying the list inside the function
    list[0]=10 #Modifying the list inside the function
    return list

#Whenever we write a function, the line calling the function is the starting point of the execution
list.append(4) #Modifying the list outside the function
l=modifyList(list)
print(l)

print("*************************************************************************************************************************************")

#Scope of variables
var1=10 #Global variable
def dummy():
    var2=20 #Local variable
    print(var1,var2)

