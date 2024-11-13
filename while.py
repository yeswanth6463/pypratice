# # num = 10
# # while num < 14:  # This replaces "for num in range(10, 14)"
# #     i = 2
# #     while i < num:  # This replaces "for i in range(2, num)"  # This will print the value of num
# #         if num %i==1: 
# #             print(num)
# #         i+=1
# #     num+=1


# list=[1,2,3,4,5,6,7,8 or 1,2,3,4,5,6]
# print(list)

l1=[[1,2,3],[4,5,6],[7,8,9]]
i=1
while i in l1[i]:
    j=0
    while j<=l1[i]:
        print(i,end=" ")
        j+=1
    i+=1
    print()
    
# for i in l1:
    # for j in i:
    #     print(i,end="")

# l1 = [[1,2,3],[4,5,6],[7,8,9]]
# i = 0
# while i < len(l1):
#     j = 0
#     while j < len(l1[i]):
#         print(l1[i][j], end="")
#         j += 1
#     i += 1

#print the count of prime num from 3
n=12498765437
c=0
l=[]
while n!=0:
    rem=n%10
    for i in range(2,rem//2+1):
        if rem%i==0:
            c+=1
        else:
            l.append(rem)
    n//=10
print(len(l))

# n=int(input('a: '))
# b=n
# s=0
# a=len(str(n))
# for i in range(1,a+1):
#     rem=n%10
#     prod=rem**a
#     s+=prod
#     a-=1
#     n//=10
# if s==b:
#     print(f'{s} is disarium')
    
