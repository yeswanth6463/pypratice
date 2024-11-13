class myclass:
    def __init__(self):
        self.a=100#public
        self._b=200#protected
        self.__c=300#private
        
    def mymethod(self):
        print(f"a value {self.a}")
        print(f"a value {self._b}")
        print(f"a value {self.__c}")
        
m1=myclass()
m1.mymethod()
print("accessing the public attribute outside class->",m1.a)
print("accessing the protected attribute outside class->",m1._b)
# print("accessing the private attribute outside class->",m1.__c)
class one:
    def display(self):
        print("i am display and public in areas")
        
    def _view(self):
        print("i am view and protected in areas")
        
    def __test(self):
        print("i am test and private in areas")

c1=one()
c1.display()
c1._view()
# c1.__test()
class employee:
    def __init__(self,name,age):
        self.__Name=name
        self.__age=age
    def getName(self):
        return self.__Name
    def setName(self,name):
        self.__Name=name
    def getage(self,age):
        return self.__age
    def setage(self,age):
        self.__age=age

c1=employee("tiger",12)
# c1.getage(14)
# c1.getName("yeswanth")
print(c1.getName())
c1.setName("yesh")
print(c1.getName())
    
    
    
class emp:
    def __init__(self,name):
        self.__name=name
    def getname(self):
        return self.__name
    def setname(self,name):
        self.__name=name
    var=property(getname,setname)
    
e1=emp("tiger")
print(e1.var)
print()
e1.var='lion'
print(e1.var)        

    
    