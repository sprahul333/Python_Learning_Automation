
class VMOLoginPage:
    email=None
    password=None

    def __init__(self,email,password):
        print("Constructor")
        self.email=email
        self.password=password


    def login_confirm(self):
        if self.password =="password123":
            print("Login successful")

        else:
            print("Login failed")


o1=VMOLoginPage("XXXXXXXXXXXXXX", "password123")
o1.login_confirm()


o2=VMOLoginPage("amit@gmail.com", "password@123")
o2.login_confirm()

email=input("Enter email: ")
password=input("Enter password: ")

o3=VMOLoginPage(email, password)
o3.login_confirm()

print("******************************************************************************************************************************")

class Car:


    def __init__(self, name, model):
        self.name=name
        self.model=model

    def start_engine(self):
        print(f"{self.name} has started")
        print(f"{self.model} has started")
        print("Engine started")


o4=Car("Audi", "Q7")
o4.start_engine()
print("******************************************************************************************************************************")