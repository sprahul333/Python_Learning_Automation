sample_string="Hello World this is a new place"

print(sample_string.split(" "))

print("*********************************************************************************************************")

#Looping the split string

for word in sample_string.split(" "):
    print(word, end=" ")

print("*********************************************************************************************************")

#Another Example of Splitting a string:

sample_string="Hello-World-this-is-a-new-place"
print(sample_string.split("-"))

print("*********************************************************************************************************")

for word in sample_string.split("-"):
    if word.lower == 's' :
        print(word)

print("*********************************************************************************************************")