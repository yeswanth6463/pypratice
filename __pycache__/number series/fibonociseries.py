n=int(input("n::"))

a=0
b=1

list=[]

for i in range(n):
    list.append(a)
    c=a
    a=b
    b=a+c
print(*list)


# for i in range(l):
#     for j in range():
#         if i==j or i+j == n-1:
#             print( list,end=" ")
#         else:
#             print(" ",end=" ")
#     print()
    

    