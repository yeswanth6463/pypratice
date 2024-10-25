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
    

for i in range(n):
    for j in range(n):
        if i==0 or i==n-2 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

for i in range(n):
    for j in range(n):
        val=(n-j-1)%9+1
        if i==j or i+j==n-1:
            print(val,end=" ")
            val+=1
        else:
            print(" ",end=" ")
    print()           

