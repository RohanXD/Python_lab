class Shape:
    def __init__(self):
        self.l=10
        self.b=20
    def xyz(self):
        print("Shape hi")
    def pqr(self): # this will not
        print("Shape bye")

class Room(Shape):
    def __init__(self):
        super().__init__() # helps to acces the parent class of the inherited class in inherited class
        self.h=40
    def pqr(self):
        super().pqr() # force being called
        print("Room Bye") # this will execute

a=Room()
print(a.h)
print(a.l)
print(a.b)
