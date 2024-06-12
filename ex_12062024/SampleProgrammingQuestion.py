#Grading System Concept in Schools

score=int(input("Enter your score: "))

if(score>90 and score<=100):
    print("Grade is A+")

elif(score>80 and score<=90):
    print("Grade is A")

elif(score>70 and score<=80):
    print("Grade is B+")
    print("You are good")

elif(score>60 and score<=70):
    print("Grade is B")
    print("You can do better")

elif(score>50 and score<=60):
    print("Grade is C+")
    print("You are average")

elif(score>40 and score<=50):
    print("Grade is C")
    print("You can do better")

elif(score<40):
    print("Grade is F")
    print("You failed")

else:
    print("Invalid Score");





