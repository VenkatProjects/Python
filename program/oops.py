class Dog:
    def __init__(self,name):
        self.name = name
        print("object with name: {} created".format(name))

    def talk (self):
        print("wolf!")

    def printName(self):
        print("my name is : {}".format(self.name))
    
    def __str__(self):
        return self.name    

tintin = Dog("tintin")
jack = Dog("jack")

tintin.talk()
jack.talk()
tintin.printName()
jack.printName()

print(tintin)
print(jack)

