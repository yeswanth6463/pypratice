l=[1,2,3,4,5,6,7]
n=int(input("n:: "))
for j in range(n):
    temp=l[-1]
    
    for i in range(len(l)-1,-1,-1):
        l[i]=l[i-1]
    l[0]=temp

print(l)