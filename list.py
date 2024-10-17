# # # my_string = "python"
# # # index = 0

# # # while index < len(my_string):
# # #     print(my_string[index])
# # #     index += 1

# # # n="python"
# # # ind=0
# # # while ind<len(n):
# # #     print(n[ind])
# # #     ind+=1    


# # # for i in range(1,4):
# # #     for j in range(1,4):
# # #         if i%2==0:                 
# # #             pass
# # #         print(i+j)

# # # for i in range(10):
# # #     pass
# # # print(i)

# # for i in range(1,501):
# #     print(i)
# #     continue# This will not print anything because the continue statement skips the rest of the code

# for i in range(1,4):
#     for j in range(1,4):
#         for k in range(1,4):
#             print(f"{i},{j},{k}",end=" ")
#     print()
    
# for i in range(1,4):
#     for j in range(1,4):
#         if i==2:
#             continue
#     print(i,j,end=" ")
#     print()

# n=int(input("n: "))
# for i in range(1,n+1):#number in range
#     print(i,end=" ")
# print()
    
# for i in range(1,n+1):
#     for j in range(1,n-i):#number in how many times
#         print(i,end=" ")
#     print()

# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print(i,end="")
#         else:
#             print(" ",end="")
#     print()
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(n+1,end="")
#     print()
    
# l1=[i for i in range(0,11,2)]
# print(l1)
