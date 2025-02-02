class cutomer:
    def __init__(self):
        d={'m':10,20:23}
        
    def printdetails(self):
        print(self.d)
        for key, value in self.d.items():
            print(f"{key}: {value}")
            
    def updateitems(self):
        self.d[input("enter a key")]=eval(input("enter a values"))
    def removeitems(self):
        self.d.pop(input("enter a delete key name"))
    def totallength(self):
        print(len(self.d))



obj=cutomer(name='yeswanth',age=22,dob='28-01-2003',address='vellore')

obj.updateitems()
obj.printdetails()
obj.removeitems()
obj.totallength()
        