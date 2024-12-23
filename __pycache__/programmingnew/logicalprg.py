# n=int(input("n:: "))
# s=0
# for i in range(n+1):
#     s+=i
# print(s)
    

# val=1
# for i in range(1,n+1):
#     val*=i
# print(val)

# #sum of even
# print(sum(range(2,n+1,2)))
# #sum of odd
# print(sum(range(1,n+1,2)))

# a=0
# b=1
# l=[]
# for i in range(n):
#     l.append(a)
#     c=a+b
#     a,b=b,c
# print(l)

# n=int(input("n::"))
# f=0
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)
#         f+=1
# print(f)

# n=int(input("n:: "))
# c=0
# for i in range(2,n+1):
#     if n%i==0:
#         c+=1
# if c==1:
#     print("prime")
# else:
#     print("not prime number")


# n=5
# c=1
# r=0
# res=0
# while True:
#     if c%2!=0:
#         res+=c
#         r+=1
#     c+=1
#     if r==n:
#         break
# print(res)
#print n of even number
# n=5
# for i in range(1,n+1):
#     f=0
#     for j in range(2,i//2+1):
#         if i%j==0:
#             f+=1
#             break
#     if f==0 and i!=1:
#         print(i,end=" ")

n=100
count=0
i=2
while count<n:
    f=0
    for j in range(2,i//2+1):
        if i%j==0:
            f+=1
            break
    if f==0:
        print(i,end=" ")
        count+=1
    i+=1
    