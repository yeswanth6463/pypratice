# n=1234
# while len(str(n))!=1:
#     sum=0
#     for i in str(n):
#         sum+=int(i)
#     n=sum
# print(sum)

# #disarium number
# # n=89
# # sum=0
# # while n!=0:
# #     rem=n%10
# #     prod=n**pow
# #     pow
# #     n//=10
# # if num==sum:
# #     print("disarium num ")
# # else:
# #     print("not a disarium num")

# # strong num/

# n=145
# sum=0
# for i in str(n):
#     fact=1
#     for j in range(1,int(i)+1):
#         fact*=j
#     sum+=fact
# if sum==n:
#     print("the given num is strong num")
# else:
#     print("not a strong num")
    
# #print amstrong numbers from 1 to 1000
# for i in range(1,1001):
#     fact=0
#     for j in str(i):
#         fact+=int(j)**len(str(i))
#         if fact==i:
#             print(i,end=" ")
# print()

# n=49
# sum=0
# prd=1
# num=n
# while n!=0:
#     rem=n%10
#     sum+=rem
#     prd*=rem
#     n//=10
# res=sum+prd
# if res==num:
#     print("special num")
# else:
#     print("not a special num")
    
# l=[]
# n=123456
# for i in str(n):
#     l.append(int(i))
#     # print(l)
# print(max(l))

# n=12345
# for i in str(n):
#     l.append(int(i))
#     # print(l)
# print(min(l))

#given number is palindrome or not
n1=12321
num=n1
rev=1
while n1!=0:
    rem=n1%10
    rev=rev*10+rem
    n1//=10
print(rev)
if rev==num:
    print("given num is palindrome")
else:
    print("given num is not palindrome")
    
                