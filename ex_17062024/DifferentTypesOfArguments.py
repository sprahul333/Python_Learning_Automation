# * args ---> Any Number of Arguments
def print_args(*args):  # Similar To List
    for arg in args:
        print(f"- {arg}")


print_args(9, "Hello", "Day", 92.24)


# Difference b/w List and Tuple is that Tuples are immutable and Lists are mutable
# *kwargs ---> Any Number of Keyword Arguments
# def print_kwargs(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")


def make_pizza(*args):
    print("Making a pizza with the following toppings:")
    for topping in args:
        print(f"- {topping}")


promod = make_pizza("pepperoni", "mushrooms", "extra cheese")
amit = make_pizza("cheese", "peppers", "onions")

# Dealing with Tuples

sample = ("ankit", "niveditha", "Arnab")
print(sample)

# Cannot change the value at any index position
# sample[0] = "Arun"

# print(sample)

print(max(5, 2, 0, 10, 4, -400))

print(
    "*********************************************************************************************************************")


# If we use * args along with another arguments, then we need to use seperators while calling the arguments
def make_pizza(*toppings, base):
    print(toppings, base)


make_pizza("pepperoni", "Panner", "Olives", base="thin crust,Hand Tossed")
