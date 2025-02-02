
d={1:10,2:20,3:30,4:40}
rd=d.items()


for i,j in rd:
     print(i,j)
     
# for i in d:
#      print(i,d[i])
# n=int(input("enter a num of pairs::"))     
# d1={}
# for i in range(n):
#      d1[int(input("enter key num"))]=eval(input("enter a value"))
# print(d1)

d={1000:34,11:34,12:22}

d.setdefault(122,23)
d.setdefault(1000,234)

print(d
      )



d3={}.fromkeys([1,2,3,4,5],[2,33,5,6,6])
print(d3)
44
res=list(zip("1234",[23,4,5,67]))
print(res)

d4={k:v for k,v in zip([1,2,3,4,5],[10,20,30,40,50])}
print(d4)
#DEFAULT ARGUMENT FUNCTION
def fun(a,b,c=10):
      print(a,b,c)
fun(10,20,30)
#positional
def fun1(a,b,c):
      print(a,b,c)
fun1(1,2,3)
#keyword argument
def fun2(a=10,b=30,c=50):
      print(a,b,c)
fun2(a=10,b=50,c=45)
#arbitary variable argument
def fun3(*args):
      print(args)
fun3({12:"errt",14:"wds"})

#arbitary keyword argument
def fun4(**kwargs):
      print(kwargs)
fun4(name='yesh',age='22')


