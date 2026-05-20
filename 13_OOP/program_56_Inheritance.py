# Inheritance

class Parent:

    def color(self):
        print("White")
        
    def height(self):
        print("Tall")
    
    def language(self):
        print("marathi")

class Child(Parent):

    def education(self):
        print("MCA")

c = Child()
c.color()
c.height()
c.education()