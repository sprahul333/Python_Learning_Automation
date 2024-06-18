#Print Even Numbers

#Steps cannot be negative
#Syntax of For Loop:

#for <variable> in range(start, stop, step):
#    <statement>

for counter in range(0, 101):
    if counter % 2 == 0:
        print(counter)

for counter in range(0, 101, 2):
    print(counter)

print("******************************************************")

#Print Odd Numbers
for counter in range(1, 101, 2):
    print(counter)

for counter in range(0, 101):
    if counter % 2 != 0:
        print(counter)

print("******************************************************")

#Print Multiples of 3
for counter in range(0, 101, 3):
    print(counter)

print("******************************************************")

for counter in range(1,20):
    if counter==5:
        break; #Comes out of the loop immediately once the condition is satisfied
    else:
        print(counter)

print("Outside of For Loop")

print("******************************************************")

#Print Numbers from 10 to 1 in reverse order
for counter in range(10,0,-1):
    if counter==5 or counter==2:
        # continue #Skips the current iteration and moves to the next iteration
        pass #Skips the current iteration and moves to the next iteration
    else:
        print(counter)

print("******************************************************")

#Print Numbers from 10 to 1 in reverse order --> New Way
for counter in reversed(range(0,10)):
    print(counter)

print("******************************************************")


for i in range (1,10):
    if(i%4==0):
        print(i)
    else:
        print(str(i*4)+" ---> Number not divisble by 4 that is why multiplying with four")