my_dict= {
    "name": "John",
    "age": 30,
    "city": "New York"
}

for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")



print("******************************************************************************************************************************")

for key, value in my_dict.items():
    if(key == "age"):
        print(f"Key: {key}, Value: {value}")


print("******************************************************************************************************************************")

#Returns true if the key is found
age="age" in my_dict
print(age)

print("******************************************************************************************************************************")

#Filter function
ages = [10, 20, 30, 40, 50]
filtered_ages = filter(lambda age: age > 30, ages)
print(list(filtered_ages))  # Output: [40, 50]

print("******************************************************************************************************************************")

filtered_ages= filter(lambda age: age%3==0, ages)
print(list(filtered_ages))

print("******************************************************************************************************************************")

def is_even(age):
    return age%2==0

filtered_ages= filter(is_even, ages)
print(list(filtered_ages))

print("******************************************************************************************************************************")

#Filter the vowels

vowels = ['a','b','d','i','o','e','l','q','n']
filtered_vowels = filter(lambda vowel: vowel in ['a', 'e', 'i', 'o', 'u'], vowels)

print(list(filtered_vowels))

print("******************************************************************************************************************************")

#Recursion
#1.Base Case
#2. Recursive Case

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(7))

print("******************************************************************************************************************************")
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))

print("******************************************************************************************************************************")

#Sum of the numbers

num=int(input("Enter a number"))

sum=0

def sum_of_digits(num):
    if num==0:
        return 0
    else:
        return (num%10)+sum_of_digits(num//10)
# while num>0:
#     digit=num%10
#     sum=sum+digit
#     num=num//10

print(sum_of_digits(num))