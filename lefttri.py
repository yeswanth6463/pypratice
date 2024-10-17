n=int(input("n::"))
for i in range(n):
    for j in range(i+1):
        # if i>=j:
            print((i%9)+1,end=" ")
    print()
for i in range(n):
    for j in range(n-i):
        # if i<=j:
            print((i%9)+1,end=" ")
    print()
for i in range(n):
    for j in range(i+1):
        # if i<=j:
            print((j%9)+1,end=" ")
    print()
    
for i in range(n):        
    for j in range(n-i):
        # if i<=j:
            print(j%9+1,end=" ")
    print()

for i in range(n):
    for j in range(i+1):
        # if i<=j:
            print((n-i-1)%9+1,end=" ")
    print()

for i in range(n):
    for j in range(n-i):
        # if i<=j:
            print((n-i-1)%9+1,end=" ")
    print()
    
    
for i in range(n):
    for j in range(i+1):
        # if i<=j:
            print((n-j-1)%9+1,end=" ")
    print()

for i in range(n):
    for j in range(n-i):
        # if i<=j:
            print((n-j-1)%9+1,end=" ")
    print()
   
for i in range(n):
    for j in range(n-i):
        # if i<=j:
        print(chr(65+(n-i-1)%26),end=" ")
    print()

for i in range(n):
    for j in range(i+1):
        # if i<=j:
            print(chr(65+(n-j-1)%26),end=" ")
    print()

  
for i in range(n):
    for j in range(n-i):
        # if i<=j:
        print(chr(65+(i%26)),end=" ")
    print()

for i in range(n):
    for j in range(i+1):
        # if i<=j:
            print(chr(65+(j%26)),end=" ")
    print()

val=0
for i in range(n):
    for j in range(i+1):
        # if i<=j:
            print(chr(65+(val%26)),end=" ")
            val+=1
    print()
val=64+n
for i in range(n):
    for j in range(i+1):
        # if i<=j:
            print(chr(val-((j-i)%26)),end=" ")
    print()


