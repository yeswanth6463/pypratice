class shape:
    def area(self):
        pass
class circle:
    pi=3.14
    def area(self,radius):
        print( self.pi*radius**2)
class rectangle(shape):
    def area(self,l,b):
        print(l*b)
        
c1=circle()
c1.area(23)
c2=rectangle()
c2.area(23,45)