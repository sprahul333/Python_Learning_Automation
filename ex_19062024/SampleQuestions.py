#Using List Comprehensions to print the numbers in the range 1 to 100 that are divisible by 3

my_list=[number for number in range(1,101) if number%3==0]
print(my_list)

print("*********************************************************************************************************")

#Print the even word present in the string
#Checks if the given word is number of characters is even or not

sample_string="Hello World this is a new place"

for word in sample_string.split(" "):
    if len(word)%2==0:
        print(word+" is Even!")

print("*********************************************************************************************************")

#Using List Comprehensions to print the numbers in the range 1 to 100 that are divisible by 3 and 5

# my_list=[number for number in range(1,101) if number%3==0: "Fizz" and number%5==0: "Buzz"]

for num in range(0,101):
    if num%3==0 and num%5==0:
        print("FizzBuzz")
    elif num%3==0:
        print("Fizz")
    elif num%5==0:
        print("Buzz")
    else:
        print(num)

# print(my_list)

print("*********************************************************************************************************")

#Using List Comprehensions to print the first letter of each word in the string

new_string_list="Hello World this is a new place"

my_list=[word[0] for word in new_string_list.split(" ")]

print(my_list)