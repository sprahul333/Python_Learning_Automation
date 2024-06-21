#Different Ways to reverse a string:

print("****************************************************************************************************************")

new_string="My Name is Promode"
rev_string="";

for i in range(len(new_string)-1,-1,-1):
    rev_string+=new_string[i]

print(rev_string);

#Second Way
print(new_string[::-1])

#Third Way

rev_list=[];
for char in new_string:
    rev_list.append(char);

rev_list.reverse()
print(rev_list)