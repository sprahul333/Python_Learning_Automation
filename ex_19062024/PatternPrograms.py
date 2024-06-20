def pattern(numberoflines):
    for i in range(1,numberoflines+1):
        for j in range(1,i+1):
            print("* ", end="")
        print("")

pattern(5)

print("*********************************************************************************************************")

# def mystery(number):
#     if number < 0:
#         return 0
#     else:
#         # print(number)
#         # mystery(number-1)
#       number  + mystery(number//2) + mystery(number//4)

# mystery(5)

my_new_list=["Hello","World","Today","Is","A","Great","Day"]

my_new_list[my_new_list.index("Today")]="Tomorrow"