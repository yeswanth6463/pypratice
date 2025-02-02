class car:
    def __init__(self,model,company):
        self.model=model
        self.company=company
    def carprice(self,ap,tax):
        self.ap=ap
        self.tax=tax
        self.tp=ap+tax
        
class tata(car):
    def __init__(self, model, company,color,cname):
        super().__init__(model, company)
        self.color=color
        self.cname=cname
    def printdetails(self):
        print("model:",self.model)
        print("company",self.company)
        print("color",self.color)
        print("cname",self.cname)
        print("price",self.tp,"lakhs")

obj=tata('suv','tata','red','nexon')
obj.carprice(10,20)
obj.printdetails()