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
