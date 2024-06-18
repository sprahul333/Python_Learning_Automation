import math

year=2000;

if(year%4==0 and year%100!=0 or year%400==0):
    print("Leap year")

else:
    print("Not a leap year")


#Factorial of a number

n=int(input("Enter a number: "))

factorials=1
# print(math.factorial(n))

for i in range(1,n+1):
    factorials=factorials*i

print(factorials)