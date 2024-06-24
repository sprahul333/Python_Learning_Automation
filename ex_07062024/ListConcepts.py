#List - ordered collection of items
#Define a list of integers
# 1. Add a Item
# 2. Remove a Item
# 3. Update a item
# 4. View Item
# 5. Exit

#Duplicates are allowed
#Values can be retrieved by location. It is a ordered sequence where it can be indexed or sliced.
from inspect import currentframe, getframeinfo

list1 = [1, 2, 3]

print(list1)

#Arrays and List are same in Python
#Prints the number of values present in the list
print(len(list1))

print(list1[0])
print(list1[1])
print(list1[-1])

#Add a value to the list
list1.append(4)

#Inserting 10 at 2nd Index position
list1.insert(2,10)

print(list1)

#Remove a value from the list
list1.remove(2)

print(list1)

list1= ["Hello","Doctor",432,33.32,'f',False]

print(list1)

#Data Type of list1 is List Class
print(type(list1))

print(list1[1:3])

#Prints the list starting from 1st index position till the end
f = currentframe()
print(getframeinfo(f).lineno, list1[1:])

#Adding Another List
#Same Like addAll function in JAVA
list1.extend(["Making","Engineers"])
print(list1)

#Prints the size of the list present
print(len(list1))

#Removes the last element and prints the index position of it
print(list1.pop())
print(list1)

print(list1[3])

#Reverse the complete list
list1.reverse()

print(list1)

#Sorting the data in ascending order
#Does work when the list has same data type of values

#Using try and except concept to handle the errors
try:
    list1.sort()
except TypeError:
    print("Unable to sort the list")


print(list1)

#List is a mutuable sequence that means we can change the value at any index position
list1[2]=100

print(list1)

popped_item=list1.pop();
print(popped_item)

print(list1)

#Removes the value that is present at second index position
popped_item=list1.pop(2);
print(popped_item)

print(list1)


#List Comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
first_col = [row[0] for row in matrix]
print(first_col)

characters=['a','g','r','w','i']

#Prints none as it does not return anything
print(characters.sort())

sorted_characters=sorted(characters)

print(sorted_characters)

#Add same values to the list:

list2=[1]*10
print(list2)

print("******************************************************************************************")

#Easy List Generation with the help of range
list_range_generation=list(range(1,11,3))
print(list_range_generation)

if not list_range_generation: #Checking the list is empty or not
    print("List is empty")

else:
    print("List is not empty")

print("******************************************************************************************")

#Shuffling the values in a list

from random import shuffle

shuffle(list_range_generation)
print(list_range_generation)


def shuffle_list(my_list):
    shuffle(my_list)
    return my_list

result=shuffle_list(list_range_generation)
print(result)

print("******************************************************************************************")

my_list=[' ','O',' '] #Initial List

def player_guess():
    guess=''
    while guess not in ['0','1','2']:
        guess=input("Pick a number: 0, 1 or 2")
    
    return int(guess)

my_index=player_guess()
print(my_index)

print("******************************************************************************************")


def check_guess(my_list,guess):
    if my_list[guess]=='O':
        print("Correct!")
    else:
        print("Wrong Guess!")
        print(my_list)

#SHUFFLING THE LIST
mixed_up_list=shuffle_list(my_list)

#USER GUESS
my_index=player_guess()

#CHECK GUESS
check_guess(mixed_up_list,my_index)
