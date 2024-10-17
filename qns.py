# for i in range(1,3):
#     for j in range(1,3):
#         print(i,j)
# # The code you provided is using nested loops to iterate over the values from 1 to 2 for both `i` and
# # `j`. The `print(i, j)` statement inside the nested loops will output all possible combinations of
# # `i` and `j` within the specified range.
        
# #print a even values using while loop
# i = 0
# while i <= 10:
#     if i % 2 == 0:
#         print(i)
        
#     i +=1
    
#print riight angle triangle
n=int(input("n:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    print()
#print left angle triangle
for i in range(1,n):
    for j in range(1,n-i):
        print("*",end="")
    print()
#straight triangle
for i in range(1,n):
    for j in range(1,i+1):
        print( " *",end=" ")
    print()
for i in range(1,n):
    for j in range(1,n-i):
        print(" *",end=" ")
    print()
for i in range(n):
        # Print leading spaces
        print(' '* (n - i - 1), end='')
        # Print asterisks
        print('* ' * (i + 1))
        
for i in range(1,6):
    for j in range(1,5):
        if j==3:
            break
print(i,end="")
# print patterns using while loop
# print a right angle triangle using while loop
n=int(input("enter a number:"))
i=1
while i<=n:
    j=1
    while j<=i:
        print("*",end=" ")
        j+=1
    i+=1
    print()
# print a 1 to 100 using while loop
# print a 1 to 100 using while loop
i=1
while i<=100:
    print(i,end=" ")
    i+=1
#print integers in triangle patterns
# print integers in triangle patterns
n1=int(input("enter a inupt"))
for i in range(1,n1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()


