n=int(input("n::"))
for i in range(n):
    for j in range(n):
        if j==0 or i==n-1 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
val=0
p =True
for i in range(n):
    for j in range(n):
        if i>=j:
            if p:
                print((val%9)+1,end=" ")
                val+=1
                p=False
            else:
                print("* ",end=" ")
                p=True
        else:
            print(" ",end=" ")
    print()