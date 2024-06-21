print("****************************************************************************************")

# Count Vowels and Consonants
new_string="Hello World this is a new place, where we can learn new things"

vowels=0
consonants=0

for char in new_string:
    if char in "aeiouAEIOU":
        vowels+=1
    elif char.isalpha():
        consonants+=1

print("Vowels: ",vowels)
print("Consonants: ",consonants)
