class battery:
    def __init__(self,current):
        self.current=current
    def discharging(self):
        if self.current>0 and self.current<101:
            print(f"current percent of charge is {self.current}")
        else:
            print("charge is empty")
    def charging(self):
        if self.current<=30:
           print(f"pls connect ur charger {self.current}")
        else:
           print(f"u charger percent is {self.current}")

        
class mobile:
    def __init__(self,name,price,color,current):
        self.name=name
        self.price=price
        self.color=color
        self.current=current
        self.o1=battery(current)
    
    def call(self):
        print(f"call method")
        self.o1.discharging()
        
    def pubg(self):
        print(f"pubg method")
        self.o1.discharging()
        
    def netflix(self):
        print(f"ur in netflix method")
        self.o1.discharging()
    def plug(self):
    
        print(f"{self.name} ur mobile is charing  mode")
        self.o1.charging()
        
c1=mobile("yeswanth",20000,"red",45)
c1.o1.discharging()
c1.o1.charging()
c1.call()
c1.netflix()
c1.pubg()
c1.plug()