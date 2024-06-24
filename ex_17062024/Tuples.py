from itertools import count
from random import shuffle

# Tuples are similar to lists but they are immutable which means they cannot be changed
# List uses square brackets
# Dictionary uses curly braces
# Tuples uses parenthesis

tup = (1, 2, 3, 4, 5)

print(type(tup))
print(tup)

print(tup[2])

print(len(tup))

print(max(tup))

print(min(tup))

print(tup)

tup = (5, 2, -20, 4, 1, 20)

sorted_tup = sorted(tup)
print(sorted_tup)

# Prints the total number of elements present with value '2' in the tuple
print(sorted_tup.count(2))

#Prints the index position of the first occurence of the value '2'
print(sorted_tup.index(2))

#Clears the complete tuple
sorted_tup.clear()

print(sorted_tup)

print("***************************************************************************************************************************************************")

#Convert List to Tuple
list1 = [1, 2, 3, 4, 5]

tup1 = tuple(list1)
print(type(tup1))
print(tup1)
print("***************************************************************************************************************************************************")

#Deleting a Tuple
tup2 = (1, 2, 3, 4, 5)
print(tup2)
del tup2
print("***************************************************************************************************************************************************")

#Joining Two Tuples
tup3 = (1, 2, 3, 4, 5)
tup4 = ('a', 'b', 'c', 'd', 'e')

#Combining two tuples and storing them
tup5 = (tup3,tup4)

print(tup5)

print(tup5[0])
print(tup5[1])

#Prints the tuple that is present at 2nd index position in the first tuple
print(tup5[0][2])
print("***************************************************************************************************************************************************")

#Slicing of Tuple

tup6 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

#Prints the elements from 2nd index position to 5th index position
print(tup6[2:6])

#Prints the elements from 2nd index position to 5th index position with a step of 2
print(tup6[2:6:2])

#Prints the elements from 2nd index position to 5th index position with a step of 3
print(tup6[2:6:3])

#Prints the elements from 2nd index position to 5th index position with a step of 4
print(tup6[2:6:4])

#Prints the elements from 2nd index position to 5th index position with a step of 5
print(tup6[2:6:5])

#Prints the elements from 2nd index position to 5th index position with a step of 6
print(tup6[2:6:6])

print("***************************************************************************************************************************************************")

#Unboxing of a tuple:

tup7 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

a, b, c, d, e, f, g, h, i, j = tup7

print(a)
print(b)
print(c)
print(d)

print("***************************************************************************************************************************************************")

stock_prices=[('APPL',200),('GOOG',400),('MSFT',100)]

for item in stock_prices:
    print(item)

print("***************************************************************************************************************************************************")


for stock,price in stock_prices:
    print(price+(0.1*price))

print("***************************************************************************************************************************************************")

#Checking for the employee of the year based on the working hours
work_hours=[('Abby',100),('Billy',400),('Cassie',800)]

def employee_check(work_hours):
        
        current_max=0
        employee_of_month=''
        
        for employee,hours in work_hours:
            if hours>current_max:
                current_max=hours
                employee_of_month=employee
            else:
                pass
        
        return (employee_of_month,current_max)

print(employee_check(work_hours))

name,hours=employee_check(work_hours)

print(name)
print(hours)

print("***************************************************************************************************************************************************")

#Below line throws an error as the tuple has only two values 

# name,hours,location=employee_check(work_hours)

# print(name)
# print(hours)

# print(location)

print("***************************************************************************************************************************************************")

#Shuffling the values of Tuple:
#Shuffles does not work in Tuples as the data is immutable and cannot be changed
#Tuples does not support Item Assignment

try:
    example=(1,2,3,4,5,6,7)

    shuffle(example)

    print(example)
except TypeError:
    print("Tuple does not support item assignment")
finally:
    print("***************************************************************************************************************************************************")
    