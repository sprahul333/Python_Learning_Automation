rangeOfFibonnaciSeries=int(input("Enter the range of Fibonaaci Series"))

a=0
b=1

for i in range(rangeOfFibonnaciSeries):
    print(a, end=" ")
    c=a+b
    a=b
    b=c