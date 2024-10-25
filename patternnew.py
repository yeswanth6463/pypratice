n=int(input("n:"))
for i in range(n):
    for j in range(n):
        if i>=j:
            print((i%9)+1,end=" ")
        else:
            print(" ",end=" ")
    print()
val=0
for i in range(n):
    for j in range(n):
        if  j==0 or j==n-1:
            print(chr(65+25-((val-n)%26)),end=" ")
            val+=1
        else:
            print(" ",end=" ")
    print()
    
