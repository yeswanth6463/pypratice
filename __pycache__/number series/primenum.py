n=int(input("n::"))
# # # # l1=([i for i in range(1,n+1) if n%i==0])
# # # # if len(l1)==2:
# # # #     print(f"{n} is prime number")
# # # # else:
# # # #     print(f"{n} is not prime number")
    
# # # val=0
# # # lc=0
# # # for i in range(2,n//2+1):
# # #     lc=+1

# # #     if n%i==0:
# # #         val+=1
# # #         break
# # # if val==0:
# # #     print(f"{n} is prime number")
# # # else:
# # #     print(f"{n} is not prime number")
# # # # print(lc,end=" ")
# # # print()



# # # val=1
# # # for i in range(1,n+1):
# # #     # if i%2==0:
# # #     val*=i  
# # # print(val,end=" ")
# # # print()
    
# # # for i in range(n):
# # #     for j in range(n):
# # #         if i>=j:
# # #             print(val,end=" ")
# # #         else:
# # #             print(" ",end=" ")
# # #     print()
    
    
# # for i in range(2,n+1):
# #     f=0
# #     for j in range(2,i//2+1):
# #         if i%j ==0:
# #             f+=1
# #             break
# #     if f==0:
# #       print(i,end=" ")
      
# # n = int(input("Enter the number of prime numbers you want: "))
# # l1=[]
# # count = 0  # To keep track of how many prime numbers we've printed
# # i = 2      # Starting from the first prime number
# # while count < n:
# #     f = 0
# #     j = 2
# #     while j <= i // 2:
# #         if i % j == 0:
# #             f += 1
# #             break
# #         j += 1

# #     if f == 0:  # If no divisors were found, it's a prime number
# #         print(i, end=" ")
# #         l1.append(i)
# #         count += 1  # Increase the prime number count
# #     i += 1  # Move to the next number to check
# # print(l1)
# # print(sum(l1))


# # n = int(input("Enter the number of prime numbers you want: "))
# # l1 = []
# # count = 0  # To keep track of how many prime numbers we've printed

# # for i in range(2, 10000):  # Setting an arbitrary large range to ensure we find enough prime numbers
# #     f = 0
# #     for j in range(2, i // 2 + 1):
# #         if i % j == 0:
# #             f += 1
# #             break

# #     if f == 0:  # If no divisors were found, it's a prime number
# #         print(i, end=" ")
# #         l1.append(i)
# #         count += 1  # Increase the prime number count
# #         if count == n:  # Stop when we've found n prime numbers
# #             break

# # print("\nList of prime numbers:", l1)
# # print("Sum of prime numbers:", sum(l1))
    
# l1=[]
# count=0
# for i in range(2,n*2):
#     f=0
#     for j in range(2,i//2+1):
#         if i%j==0:
#             f+=1
#             break
#     if f==0:
#       print(i,end=" ")
#       count+=1
#       l1.append(i)
#       if count==n:
#         break
# print(l1)

l1=[]
count=0
i=2
while count<n:
    f=0
    j=2
    while j<=i//2:
        if i%j==0:
            f+=1
            break
        j+=1
    if f==0:
        l1.append(i)
        count+=1
    i+=1
print(l1)
   
            
l1=[]
count = 0  # To keep track of how many prime numbers we've printed
i = 2      # Starting from the first prime number
while count < n:
    f = 0
    j = 2
    while j <= i // 2:
        if i % j == 0:
            f += 1
            break
        j += 1

    if f == 0:  # If no divisors were found, it's a prime number
        print(i, end=" ")
        l1.append(i)
        count += 1  # Increase the prime number count
    i += 1  # Move to the next number to check
print(l1)
print(sum(l1))


l1=[]
count=0
i=2
while count<n:
    f=0
    j=2
    while j<=i//2:
        if i%j==0:
            f+=1
            break
        j+=1
    if f==0:
        l1.append(i)
        count+=1
    i+=1
print(l1)




