#Loop ---> Repeating the same thing for multiple times
#No Do while loop in python
print("************************************************WHILE LOOP************************************************************************")
#While Loop
#Syntax: while condition:
#             //statements

#Example: Print "Hello" 5 times
i=1

while i<=5:
    print("Hello")
    i+=1

# while True:
#     print("Hello") #Infinite loop
#     # break

print("************************************************FOR LOOP************************************************************************")
#For Loop
#Syntax: for value in sequence:
#             //statements

#Example: Print 1 to 5
#Inclusive of starting range and exclusive of end range
for i in range(1,6):
    print(i)

# initialvalue=50
# for initialvalue in range(100):
#     print(initialvalue)

#Prints the values from 1 to 11 by increasing the value to 2
for i in range(1, 11, 2):
    print(i)

print("************************************************NESTED LOOP************************************************************************")
#Nested Loop
#Syntax: for value in sequence:
#             for value in sequence:
#                 //statements

#Example: Print the table of 2
for i in range(1, 11):
    print(2, "X", i, "=", 2*i)


x=list(range)
print(x)