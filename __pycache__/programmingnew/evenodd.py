# n=int(input("enter a number:: "))
# if (n>>1)<<1==n:
#     print("even")
# else:
#     print("odd")
val=0
val2=0
for i in range(2000):    
    for j in range(2000):
        if i%2==0:
            print(chr((val%26)+65),end=" ")
            
        else:
            print((val2%9)+1,end=" ")
    if i%2==0:
        val+=1
    else:
        val2+=1
    print()
    
    