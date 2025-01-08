class nums:
    def __init__(self):
        self.num=[1,2,3,4,5,6,7,8,9,10]
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        while self.index<len(self.num):
            current=self.num[self.index]
            self.index+=1
            if current %2==0:
                return current
        raise StopIteration
n=nums()
while True:
    try:
        print(n.__next__())
    except StopIteration as e:
        break
   
        