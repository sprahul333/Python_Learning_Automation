#Perform Different mathematical Operations

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
      #Exception handling for division by zero
        try:
            return self.num1 / self.num2
        except ZeroDivisionError:
            return "Cannot divide by zero"


# Create an instance of the Calculator class
calculator = Calculator(10, 2)
print(calculator.add())     # Output: 12