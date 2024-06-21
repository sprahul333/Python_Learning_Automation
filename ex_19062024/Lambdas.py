#Lamda Expression is used to perform the task in one line:
#Lambda Function is a small anonymous function.
# A lambda function can take any number of arguments, but it can only have one expression.
#Suitable for smaller functions

def double(x):
    return x * 2

print(double(5))
print("*************************************************************************************************************************************")

#Lambda Syntax : lambda arguments_name:result or return_type
double_salary = lambda x: x * 2
print(double_salary(5))

print("*************************************************************************************************************************************")

triple = lambda x: x * 3
print(triple(5))

print("*************************************************************************************************************************************")

#Similar to arrow function in JS
sumoftwonumbers = lambda a, b: a + b
print(sumoftwonumbers(5, 6))
print(sumoftwonumbers) #Prints the memory address of the lambda function

print("*************************************************************************************************************************************")

#Lambda function with if-else condition
maximum = lambda a, b: a if a >= b else b

print(maximum(5, 20))

print(maximum(25, 10))

print("*************************************************************************************************************************************")
print("End of the Program")

print("*************************************************************************************************************************************")
print("*************************************************************************************************************************************")

sumofthreenumbers = lambda a, b, c: a + b + c
print(sumofthreenumbers(5, 6, 7))

print("*************************************************************************************************************************************")

odd_even_function=lambda a: "Even" if(a%2==0) else "Odd"
print(odd_even_function(5))
print(odd_even_function(12))

print("*************************************************************************************************************************************")

#Lambda function with map() function
numbers = [1, 2, 3, 4, 5]

#Map is a function that performs the operations and stores the values into another list
#Picks each value from the list and sqaures the number and stores in another list
squared_numbers = map(lambda num: num ** 2, numbers)
print(list(squared_numbers))

print("*************************************************************************************************************************************")

#Lambda function with filter() function
numbers = [1, 2, 3, 4, 5]
odd_numbers = filter(lambda num: num % 2 != 0, numbers)
print(list(odd_numbers))

print("*************************************************************************************************************************************")
#Using Input Function

cube_number=lambda x=int(input("Enter a number:")):x**3
result=cube_number()
print(result)