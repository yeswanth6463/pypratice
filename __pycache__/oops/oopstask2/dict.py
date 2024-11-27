class mydictionary:
    
    def __init__(self):
        self.dict={}
    
    def additems(self,key,value):
        self.dict[key]=value
    def deleteitems(self,key):
        if key in self.dict:
            del self.dict[key]
            
        else:
            print("key not found")


    def displayitems(self):
        print(f"{self.dict}")
    
k1=mydictionary()
k1.additems(1,2)
k1.additems("yeswant",80)
k1.displayitems()
k1.deleteitems(1)
k1.displayitems()

        