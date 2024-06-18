import math

z=10
y=20

print("z" if z>y else "y")

#Area of Circle

radius = float(input("Enter the radius of the circle: "))

print("The area of the circle is: ", 3.14 * radius * radius)
print("The area of the circle is: ", math.pi * radius ** radius)

#Perimeter of Circle

#Performing different mathematical operations in a single line
print("The perimeter of the circle is: ", 2 * math.pi * float(input("Enter the radius of the circle: ")))