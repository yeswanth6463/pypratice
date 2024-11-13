# class course:
#     def __init__(self,name,duration,price):
#         self.name=name
#         self.duration=duration
#         self.price=price
    
# class student(course):
#     def __init__(self, name, duration, price,stname,stmono,stmailid,degree):
#         super().__init__(name, duration, price)
#         self.stname=stname
#         self.stmono=stmono
#         self.stmailid=stmailid
#         self.degree=degree
#     def details(self):
#         print(f"course name {self.name}")
#         print(self.duration)
#         print(self.price)
#         print(self.stname)
#         print(self.stmono)
#         print(self.stmailid)
#         print(self.degree)
# st1=student("fsd","6month","29k","yeswanth","9597470128","yeswanth6463@gmail.com","b.tech",)
# st1.details        
# class diva:
#     def __init__(self,a):
#         self.a=a
#     def method(self):
#         print(f'{self.a} is a')
# class horse(diva):
#     def __init__(self,a):
#         self.a=a
#         super().__init__(a)
# c=horse(1000)
# c.method()
# # c=horse(10)

class TWITTER:
    version='x1'
    def __init__(self,uname,password):
        self.uname=uname
        self.password=password
    def tweet(self):
        print('u can tweet')
    def post(self):
        print('u can post media')
class TWITTER2(TWITTER):
    version='x2'
    def __init__(self,uname,password,phone_no):
        self.phone_no=phone_no  
        super().__init__(uname,password)
    # def tweet(self):
        # print(super().__init__())
    def post(self):
        print('u cannot post media')
class TWITTER3(TWITTER2):
    version3='x3'
    def __init__(self,uname,password):
        self.uname=uname
        self.password=password
    def tweet(self):
        print('u cannot tweet without media')
# a=TWITTER3('diva',12345)
# a.tweet()
a=TWITTER('diva',123)
a.tweet()
a.post()
b=TWITTER2('donald',123,98766554)
b.post()
c=TWITTER3('donald trump',234)
b.tweet()