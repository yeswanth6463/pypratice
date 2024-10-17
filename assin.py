# # n = int(input("n: "))
# # # # for i in range(n):
# # # #     for j in range(n):
# # # #         if i >= j:
# # # #             print((i % 9) + 1, end=" ")
# # # #         else:
# # # #             print(" ", end=" ")
# # # #     print()
# # # # 1
# # # # 2 2
# # # # 3 3 3
# # # # 4 4 4 4
# # # # 5 5 5 5 5
# # # # 6 6 6 6 6 6
# # # # 7 7 7 7 7 7 7


# # # ##############################

# # # # for i in range(n):
# # # #     for j in range(n):
# # #     # if (i + j) >= n - 1:
# # #     #         print(((n - i - 1) % 9) + 1, end=" ")
# # #     #     else:
# # #     #         print(" ", end=" ")
# # #     # print()
# # #     #         if i == j:
# # # #             print(  chr(65+25-(i % 26)), end=" ")
# # # #         else:
# # # #             print(" ", end=" ")
# # # #     print()
    

# # # # for i in range(n):
# # # #     for j in range(n):
    
# # # # for i in range(n):
# # # #     for j in range(n):
# # # #         if i<=j:
# # # #             print(((n-i-1) % 9) + 1, end=" ")
# # # #         else:
# # # #             print(" ", end=" ")
# # # #     print()
# # for i in range(n):
# #     for j in range(n):
# #         if i+j == n-1:
# #             print(chr((( - (j - i)) - 65) % 26 + 65), end=" ")        
# #         else:
# #             print(" ", end=" ")
# #     print()
# # # ######################################
# # # # for i in range(n+1):
# # # #     for j in range(n-i):
# # # #         print(" ",end="")
# # # #     for j in range(i):
# # # #         print(chr(65 +((n-i)% 26)), end=" ")
# # # #     print()
    
# # # # for i in range(n):
# # # #     for j in range(n):
# # # #         if i+j==n-1:
# # # #             print(chr(65+25-(i%26)),end=" ")
# # # #         else:
# # # #             print(" ",end=" ")
# # # #     print()
    
# # # # n = int(input("n: "))
# # # # val=0
# # # # for i in range(n):
# # # #     for j in range(n):
# # # #         if i + j >= n - 1:
# # # #             print(chr(65 + (val % 26)), end=" ")
# # # #             val+=1
# # # #         else:
# # # #             print(" ", end=" ")
# # # #     print()



# # # # for i in range(n):
# # # #     for j in range(n):
# # # #         if i+j==n-1:
# # # #             print(chr(65+25-((i-n)%26)),end=" ")
# # # #             # print(9-((i-n)%9),end=" ")
# # # #         else:
# # # #             print(" ",end=" ")
# # # #     print()

# # # n = int(input("n: "))
# # start_char = 64 + n
# # for i in range(n):
# #     for j in range(n):
# #         if i == j:
# #             # Ensure only A-Z characters
# #             print(chr(((start_char - (j - i)) - 65) % 26 + 65), end=" ")
# #         else:
# #             print(" ", end=" ")
# #     print()
# # # n=int(input('a: '))
# # # for i in range(n):
# # #     if n>25 or n
# n=int(input("n: "))
# for i in range(n):
#     val=n-1
#     if val>26 or val<0:
#         val=25
#     for j in range(n):
#         if i<=j:
#             print(chr(65+val),end=" ")
#             val-=1
#             if val>25 or val<0:
#                 val=25
#         else:
#             print(" ",end=" ")
#         # val-=1
#         # if val<1:
#             # val=25
#     print()
n=int(input("n::"))
for i in range(n):
    for j in range(n):
        if i+j==n-1:
            print(chr(65+25-((i-n)%26)),end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(n):
    for j in range(n):
        if i==j:
            # print(chr(65+25-((i-n)%26)),end=" ")
            print((((n-i-1)%9)+1),end=" ")
        else:
            print(" ",end=" ")
    print()
