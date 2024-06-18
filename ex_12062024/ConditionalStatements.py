#Pre and Post Increment or Decrement Operations are not there in Python

a=10

#Syntax of if else statement
# if condition:
    #body of if
# else:
    #body of else

if a==10:
    print("a is equal to 10")

else:
    print("a is not equal to 10")

age=int(input("Enter your age: "))

#In Java we use && for and operation and in Python we can use 'and' or & for And Operation
if(age>=18 and age<60):
    print("You are eligible to vote")
    print("You can also vote")
else:
    print("You are not eligible to vote")

a=10
b=20
c=40
d=80

result = a<b
result1= c>d
print(result and result1)

#In Java we use || for OR Operation and in python we use 'or' , '|' for OR operation
print(result or result1)

#Find the max between two numbers

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")

#Checking for the maximum value using the functions
result=max(a,b)
print(result)

#Checking for multiple Conditions using multiple values




#Another Example of If else statement
age =30
name = "John"

if name == "John":
    if age==30:
        print("You are John and you are 30 years old")
    else:
        print("You are John but you are not 30 years old")

else:
    print("You are not John")

print("************************************************************************************")

#Not operator

a=10
b=20

if not a==b:
    print("a is not equal to b")
    if a>b:
        print("a is greater than b")
        if a>=b:
            print("a is greater than or equal to b")


print("************************************************************************************")
print("End of the Program")