n=1234567896
l=[]
while n!=0:
    rem=n%10
    c=0
    for i in range(2,rem//2+1):
        if rem%i==0:
            c+=1
        if c==0 and rem!=1:
            l.append(rem)
    n//=10

print(len(l))

            