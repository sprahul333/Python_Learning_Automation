#Printing the min of two numbers if both the numbers are even
def lesser_of_two_even_numbers(a,b):
    if a%2==0 and b%2==0:
        return min(a,b)
    else:
        return max(a,b)

print(lesser_of_two_even_numbers(2, 4))

print(lesser_of_two_even_numbers(2, 5))

print("**************************************************************************************************************")

#Printing the max of two numbers if both the numbers are odd
def greater_of_two_odd_numbers(a, b):
    if a%2!=0 and b%2!=0:
        return max(a, b)
    else:
        return min(a, b)

print(greater_of_two_odd_numbers(2, 4))

print(greater_of_two_odd_numbers(3, 5))
print("**************************************************************************************************************")

#Take the function that writes two strings and check whether both the strings with the same letter or not

def animal_crackers(text):
    wordlist = text.split()
    print(wordlist)
    return wordlist[0][0] == wordlist[1][0]

result = animal_crackers('Levelheaded Llama')

print(result)

print("**************************************************************************************************************")

#Given two integers return true if the sum is 20 or if either of the numbers is 20 else return false

def makes_twenty(n1, n2):
    if n1+n2==20 or n1==20 or n2==20:
        return True
    else:
        return False

print(makes_twenty(20, 10))

print(makes_twenty(12, 8))

print("**************************************************************************************************************")

'''
Given a string, return a new string where the first and last chars have been exchanged.
'''
def front_back(word):
    if len(word) <= 1:
        return word
    else:
        return word[-1] + word[1:-1] + word[0]

# Your code goes here

print(front_back("New Place in Making"))

print(front_back("a"))

print("**************************************************************************************************************")

#Create a function that capitalizes first and four letter of a name and returns the name
def capatalize(name):
    first_half = name[:4]
    second_half = name[4:]
    return first_half.capitalize() + second_half.capitalize()

print(capatalize("macdonald"))

print("**************************************************************************************************************")

'''
Given a list of ints, return True if 6 appears as either the first or last element in the list. The list will be length 1 or more.
'''
def first_last_six(nums):
    if nums[0] == 6 or nums[-1] == 6:
        return True
    else:
        return False

print(first_last_six([1, 2, 3]))

print(first_last_six([6, 1, 2, 3]))

print("**************************************************************************************************************")

'''
Given a list of numbers, iterate and print the first and the last element of the list.
'''
def first_last(given_list):
    print("First element:", given_list[0])
    print("Last element:", given_list[-1])

first_last([1, 2, 3, 4, 5])

print("**************************************************************************************************************")

'''
Given a list of ints, return the difference between the largest and smallest numbers, i.e. how much the highest number is smaller than the lowest number.
'''

def diff(nums):
    return max(nums) - min(nums)

print(diff([10, 15, 20, 2, 5]))

print("**************************************************************************************************************")

#Define a function which reverses the words of a string

def reverse_words(string):
    words = string.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

print(reverse_words("Hello World"))

print("**************************************************************************************************************")

#Given an integer n, return True if n is within 10 of either 100 or 200
def near_hundred(n):
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

print(near_hundred(93))

print(near_hundred(90))

print("**************************************************************************************************************")
'''
Your cell phone rings. Return whether its a class or not.
'''
def parrot_trouble(talking, hour):
    return talking and (hour < 7 or hour > 20)

print(parrot_trouble(True, 6))