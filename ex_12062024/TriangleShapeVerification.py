side1=int(input("enter the First Side"))
side2=int(input("enter the Second Side"))
side3=int(input("enter the Third Side"))

#elif means else if in JAVA

if side1==side2 and side2==side3:
    print("The Triangle is an Equilateral Triangle")
    print("It has equal sides")
elif side1==side2 or side2==side3 or side1==side3:
    print("The Triangle is an Isosceles Triangle")
    print("It has two sides equal")
    print("It has one angle equal")

elif side1!=side2 and side2!=side3 and side1!=side3:
    print("The Triangle is a Scalene Triangle")
    print("It has no equal sides")
    print("It has no equal angles")