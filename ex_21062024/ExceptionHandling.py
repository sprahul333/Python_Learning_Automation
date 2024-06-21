number1=int(input("Enter the first number: "))

number2=input("Enter the second number: ")

# def add(number1, number2):
#     return number1+number2

try:
    print(number1+number2)
except TypeError as e:
    print("Please check the addition operations being performed")
finally:
    print("Try Catch Block Execution is completed")

# else:
#     print("The addition operation is successful")

print("************************************************************************************************************************")

try:
    f=open("testfile.txt","w")
    f.write("This is a test file")

except OSError:
    print("OS Error Occured, please check")

except:
    print("Error in writing to the file")

finally:
    print("File write operation is completed")

print("************************************************************************************************************************")

def ask_for_int():
    while True:
        try:
            result=int(input("Please enter the number: "))
        except:
            print("Please enter the number")
            continue
        else:
            print("Thank you for entering the number")
            break
        finally:
            print("Finally Block is executed")  

ask_for_int()            

print("************************************************************************************************************************")

try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print("Error in the code")

