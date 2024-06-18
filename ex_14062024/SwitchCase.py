numbers=int(input("Enter the number: "))

#Works from Python 3.10
#Break is not necessary in Python, JAVA needs to have
match numbers:
    case 90:
        print("A")
    case 80:
        print("B")
    case 70:
        print("C")
    case 60:
        print("D")
    case _:
        print("F")

print("******************************************************************************************************")

name=input("Enter the name: ")

match  name:
    case "A":
        print("A")
    case "B":
        print("B")
    case "C":
        print("C")

    #Default Case
    case _:
        print("F")

print("******************************************************************************************************")

browser = "CHROME"

browser=browser.lower();

match browser:
    case "chrome":
        print("Executing in Chrome Browser")
    case "firefox":
        print("Executing in Firefox Browser")
    case "edge":
        print("Executing on Edge Browser")

    case _:
        print("Unknown Browser")