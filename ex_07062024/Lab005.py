# Take two integers from user and add those

# a = input("Enter the First Number");  # Reads the input from the console and converts them to string
# b = input("Enter the Second Number");
#
# # int(variable_name) ---> Converts the string to integer
# result = int(a) + int(b);
#
# print("Sum of two numbers is: " + str(result))

# Prints Paragraphs
name = """Harry is going for a walk
...........................................
...........................................
...........................................
...........................................
...........................................
...........................................
...........................................
...........................................
...........................................
""";

# r stands for raw string ---> Does not do any parsing or stuff, takes the string as it is
name = r'C:\nomedir\nomedir'  # This is how we give the path in directory

first_name = "Rahul";
last_name = "Sharma";

print(first_name + " " + last_name)
print(first_name, last_name)

#Using System.out.printf concept here
print( f'Your Full Name is {first_name} {last_name}')

# String Formatting
print("Your Full Name is %s %s" % (first_name, last_name))

num = 10;

print(f'{num}*1={num}')
print(f'{num}*2={num*2}')
print(f'{num}*3={num*3}')
print(f'{num}*10={num*4}')

b=1;
print("2x{} ={}, {}".format(b,b*2,3))