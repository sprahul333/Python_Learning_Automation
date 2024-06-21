from random import shuffle, randint

index_count = 0

for letter in 'abcde':
    print(f'current letter is {letter} at index position {index_count}')
    index_count+=1

print('-----------------')

#Shortcut for the above one is:
word='abcde'

for index, letter in enumerate(word):
    print(index)
    print("--------------------------")
    print(letter)

#Zip Function ---> Combining them together or like a zip a jacket which converts the list into the form of tuples
list1=[1,2,3,4,5]
list2=['a','b','c','d','e']
list3=[100,200,300,400,500]

for item in zip(list1,list2,list3):
    print(item)

shuffled_list=shuffle(list3)
print(shuffled_list) #Prints None as it returns a none data type
print(list3)
print("--------------------------")

#Use of In :
#Checks whether that value is present in that list or not
print('a' in 'Hello')
print('x' in ['a','c','b'])

print("*****************************************************************************************")

print("Print a random integer from 0 to 1000");
randomint=randint(0,1000)

print(randomint)