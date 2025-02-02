class pbc:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
        
    def getname(self):
        return self.__name
    def setname(self,name):
        self.__name=name
    def getage(self):
        return self.__age
    def setage(self,age):
        self.__age=age
    var=property(getage,setage)
    var2=property(getname,setname)
    
obj1=pbc('yesh',12)
print(obj1.var2)  # prints: tiger
print(obj1.var)


