class dog:
    def noise(self):
        print("bow bow")
    def name(self):
        print("my name is dog")

class cat:
    def noise(self):
        print("meow meow")
    def name(self):
        print("my name is cat")


def animal(obj):
    obj.noise()
    obj.name()

d1=dog()
c1=cat()


animal(d1)
animal(c1)