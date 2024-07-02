class BankAccount:

    def __init__(self):
        self.balance = 0
        self.__private_var=100

    def public_func(self):
        print(self.__private_var)

    def deposit(self, amount):
        self.balance += amount

    def _withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

        print(f"Available balance is {self.balance}")

    def __show_balance(self):
        print(f"Available balance is {self.balance}")

    def if_you_are_authenticated(self,flag):
        if(flag):
            self.__show_balance()
        else:
            print("You are not authenticated")

    def if_you_are_authenticated_user(self, flag,amount):
        if(flag):
            self._withdraw(amount=amount)
        else:
            print("You are not allowed")


#Creating an object of the class
obj=BankAccount()
obj.public_func()

#Accessing the public variable
print(obj.balance)

obj.deposit(1000)

# obj.__show_balance()
#
# obj.withdraw(400)
#
# obj.show_balance()
#
# obj.deposit(5000)
#
# obj.show_balance()

secret_pin = int(input("Enter your secret pin"))
your_amount = int(input("Enter the amount you want to withdraw"))

if(secret_pin == 1234):
    obj.if_you_are_authenticated_user(True, your_amount)
    obj.if_you_are_authenticated(True)
else:
    obj.if_you_are_authenticated(False)