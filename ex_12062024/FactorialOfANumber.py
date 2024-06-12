rangeOfFactorial=int(input("Enter the number for which you want to find the factorial: "))

product=1;

if(rangeOfFactorial<0):
    print("Factorial of negative number doesn't exist")

for i in range(1,rangeOfFactorial):
    product=product*i
    print(product)