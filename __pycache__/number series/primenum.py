n=int(input("n::"))
# l1=([i for i in range(1,n+1) if n%i==0])
# if len(l1)==2:
#     print(f"{n} is prime number")
# else:
#     print(f"{n} is not prime number")
    
val=0
lc=0
for i in range(2,n//2+1):
    lc=+1

    if n%i==0:
        val+=1
        break
if val==0:
    print(f"{n} is prime number")
else:
    print(f"{n} is not prime number")
# print(lc,end=" ")
print()



val=1
for i in range(1,n+1):
    # if i%2==0:
    val*=i  
print(val,end=" ")
print()
    
for i in range(n):
    for j in range(n):
        if i>=j:
            print(val,end=" ")
        else:
            print(" ",end=" ")
    print()
