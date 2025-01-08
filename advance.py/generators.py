l1=[1,2,3,4,5,6,7,8,9,10]
def prime(n):
    l=[]
    for i in range(2,n+1):
        if n%i==0:
            l.append(i)
    if len(l)==1:
        return True
    else:
        return False

def primenums(num):
    for i in num:
        if prime(i)==True:
            yield i

res=primenums(l1)

while True:
    try:
        print(next(res))
    except StopIteration as e:
        break
    




        