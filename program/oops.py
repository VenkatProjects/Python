class Dog:
    def __init__(self,name):
        self.name = name
        print("object with name: {} created".format(name))

    def talk (self):
        print("woof!")

    def printName(self):
        print("my name is : {}".format(self.name))
    
    def __str__(self):
        return self.name    

venkat = Dog("Venkat")
divya = Dog("Divya")

venkat.talk()
divya.talk()
venkat.printName()
divya.printName()

print(venkat)
print(divya)

