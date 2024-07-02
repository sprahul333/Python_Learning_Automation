#Method Overriding

class Father:
    def home(self):
        print("I have a big house")


class Son(Father):
    def home(self):
        super().home() #Referring to the parent method present in the parent class
        print("I have a small house")
    # pass


son = Son()
son.home()
