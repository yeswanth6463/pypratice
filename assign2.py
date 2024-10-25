n=int(input("n::"))
val=0
for i in range(n):
    for j in range(n):
        if i>=j:
            print((val%9)+1,end=" ")
            val+=1
        else:
            print("*",end=" ")
    print()

for i in range(n):
    for j in range(n):
        if i==j:
            # print((j%9)+1,end=" ")
            print("*",end=" ")
        elif i>=j:
            print((j%9)+1,end=" ")
        else:
            print(((j-i-1)%9)+1 ,end=" ")
    print()
    
n = int(input("n: "))
for i in range(n):
    val = (i // 2)%9 + 1 if i % 2 == 0 else "*"
    for j in range(n):
        if i + j >= n - 1:
            print(val, end=" ")
        else:
            print(" ", end=" ")
    print()

for i in range(n):
    if i % 2 == 0:
        val = (i // 2) % 9 + 1
    else:
        val = "*"
    for j in  range(n):
        if i+j>=n-1:
            print(val,end=" ")
        else:
            print(" ",end=" ")
    print()
# print pattern like 
# 1
# * 2
# * 3 *
# 4 * 5 *
# Take user input for the number of rows
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print("*",end=" ")
#     print()
# for i in range(n+1):
#     for j in range(n):
#         if j==n-1 or i+j==n-1 or i==j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()        
    
    
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for k in range(2*i+1):
        print(chr(65+(i%26)),end=" ")
    print()
val=0
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for k in range(2*i+1):
        print((val%9)+1,end=" ")
        val+=1
    print()

val = n
for i in range(n):
    if val >26:
        val=26
    for j in range(n-i-1):
        print(" ", end=" ")
    for k in range(2*i+1):
        print(chr(64+val), end=" ")
    print()
    val -= 1
    if val < 1:
        val = 26
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()
val=0
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print((val%9)+1,end=" ")
        val+=1
    print()

for i in range(n):
    for j in range(2*n-1):
        if i+j==n-1 or j-i==n-1 or i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
      # Example input

for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        if k == 0 or k == 2 * i or i == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

for i in range(n):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i+1):
        print("*",end=" ")
    print()

for i in range(2*n-1):
    for j in range(n):
        if i+j==n-1 or j==n-1 or i-j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(2*n-1):
    for j in range(n):
        if j==0 or i==j or i+j==2*n-2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print(((i%9)+1),end=" ")
            
        else:
            print(" ",end=" ")
    print()
val=0
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        if i==j or i==0 or i+j==2*n-1:
            print((val%9)+1,end=" ")
            val+=1
        else:
            print(" ",end=" ")
    print()
 # Example value for n

for i in range(n):
    val = (i // 2) % 26 if i % 2 == 0 else "$"
    for j in range(n):
        if i + j >= n - 1:
            if isinstance(val, int):
                print(chr(65 + val), end=" ")
            else:
                print(val, end=" ")
        else:
            print(" ", end=" ")
    print()
  # Example value for n

for i in range(n):
    val = (i // 2) % 26 if i % 2 == 0 else "$"
    for j in range(n):
        if i + j >= n - 1:
            if i % 2 == 0:
                print(chr(65 + val), end=" ")
            else:
                print(val, end=" ")
        else:
            print(" ", end=" ")
    print()
    
    
p=True
val=0
for i in range(n):
    for j in range(n):
        if i>=j:
            if p:
                print((val%9)+1,end=" ")
                val+=1
                p=False
            else:
                print("$",end=" ")
                p=True
        else:
            print(" ",end=" ")
    print()
    
val=1
for i in range(n):
    if val>9:
        val=1
    for j in range(2*n-1):
        if i==0 or i==j or i+j==2*n-2:
            print(val,end=" ")
            val+=1
        else:
            print(" ",end=" ")
    print()
    

