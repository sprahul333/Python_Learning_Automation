print("**************************************************************************************************************************************")

# Pallindrome Words

sample_string="Hello World this is a new place"

for word in sample_string.split(" "):
    if word==word[::-1]:
        print(word+" is a Pallindrome!")


print("**************************************************************************************************************************************")