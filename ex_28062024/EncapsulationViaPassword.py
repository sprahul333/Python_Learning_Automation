class Password:

    def __init__(self, password):
        self.__password = password
        self.public_var=10


    def get_password(self, is_auth):
        if is_auth:
            return self.__password
        else:
            return "Access denied"

    def set_password(self, new_password, is_auth):
        if is_auth:
            if(len(new_password)>10):
                self.__password = new_password
                return "Password updated"
            else:
                return "Password should be at least 10 characters"
        else:
            print("Access denied")


pwd=Password("abc@123")
print(pwd.get_password(True))
print(pwd.set_password("123@4",True))
