class car:
    def __init__(self,company,model,fueltype,price):
        self.company=company
        self.model=model
        self.fueltype=fueltype
        self.price=price
    def details(self):
        print(f"cmpny name {self.company}")
        print(f"model name {self.model}")
        print(f"fule name {self.fueltype}")
        print(f"price name {self.price}")
        
        
car1=car(str(input("enter a company ")),
         str(input("enter a model ")),
         str(input("enter a fueltype ")),
         int(input("enter a price "))
         )
car1.details()