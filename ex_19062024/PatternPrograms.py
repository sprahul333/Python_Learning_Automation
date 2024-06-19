def pattern(numberoflines):
    for i in range(1,numberoflines+1):
        for j in range(1,i+1):
            print("* ", end="")
        print("")

pattern(5)