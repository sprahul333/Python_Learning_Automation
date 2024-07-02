class Person:

    # behaviour
    def talk(self):
        print("I can talk")

    def walk(self, name):
        print("walk", name)


    def sleep(self, name):
        return None



prakash = Person()
prakash.name = "PrakashMunyapillai"

prakash.talk()
nandana = Person()
nandana.name = "Nandana"
nandana.sleep(nandana.name)