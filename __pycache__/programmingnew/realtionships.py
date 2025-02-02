class suv:
    def __init__(self,model,no_of_sold):
        self.model=model
        self.no_of_sold=no_of_sold
    def car_analysis(self):
        tp=self.no_of_sold*100000
        print(tp)
    
class carshop:
    def __init__(self,car_brand,model,no_of_sold):
        self.car_brand=car_brand
        self.suv=suv(model,no_of_sold)

    def printingdetails(self):
        print(f"{self.car_brand}")
        print(f"model:{self.suv.model}")
        print(f"no_of_sold:{self.suv.no_of_sold}")
        self.suv.car_analysis()

ob=carshop('tata','suv',23)
ob.printingdetails()




