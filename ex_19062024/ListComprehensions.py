#List Comprehensions are a unique way of quickly creating lists with Python.

new_string="Worlds"

my_list=[]

for i in new_string:
    my_list.append(i)

print(my_list)

print("*********************************************************************************************************")
# The above code can be written as a list comprehension as follows:

another_string="Hello"
my_list=[letter for letter in another_string]
print(my_list)  

print("*********************************************************************************************************")
#Another Example of List Comprehensions:

my_list=[number for number in range(1,11)]

print(my_list)

print("*********************************************************************************************************")
#Another Example of List Comprehensions:

my_list=[number**3 for number in range(1,11)]

print(my_list)

print("*********************************************************************************************************")
#Another Example of List Comprehensions:

my_list=[number for number in range(1,11) if number%2==0]
print(my_list)


print("*********************************************************************************************************")
#Another Example of List Comprehensions:

temp_celcius=[0,22.5,40,100]
my_list=[( (9/5) * temp + 32) for temp in temp_celcius]

print(my_list)

print("*********************************************************************************************************")
#Another Example of List Comprehensions:

my_list=[x if x%2==0 else "ODD" for x in range(0,11)]
print(my_list)

print("*********************************************************************************************************")
#Nested List Comprehensions:

nested_list=[]

for x in range(1,11):
    for y in range(1,11):
            nested_list.append(x*y)
        
print(nested_list)


print("*********************************************************************************************************")
#Another Example of List Comprehensions:

my_list=[x*y for x in [2,4,6] for y in [1,10,1000]]
print(my_list)
