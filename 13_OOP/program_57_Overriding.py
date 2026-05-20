# method overriding

class Animals:
    
    def sound(self):
        print("Some Genric sound !")

class Tiger(Animals):

    def sound(self):
        print("roar")

class Dog(Animals):

    def sound(self):
        print("Bhu bhu !")

Animal = Animals()
tiger = Tiger()
dog = Dog()

Animal.sound()
tiger.sound()
dog.sound()