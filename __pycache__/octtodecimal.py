# n=int(input("enter a number decimal to octal::"))
# res=""
#
# while n!=0:
#     res+=str(n%2)
#     n//=2
# print(res[::-1])
# print(res)
#decimal to hexadecimal without using in build function
# while n!=0:
#     if n%8==0:
#         res+="0"
#     else:
#         res+=str(n%8)
#         n//=8
# print(res)

# n=int(input("enter a number decimal to hexadecimal::"))
# res=""
# while n!=0:
#     res+=hex(n%16)[2:].upper()
#     n//=16
# print(res)
    
# res=0
# p=1
# while n!=0:
#     rem=n%10
#     res=res+rem*p
#     n//=10
#     p*=2
# print(res)


# second largest element in a list
l=[10,20,40,10,50,30,67,98] 
l1=[i for i in set(l) ]
l1.sort()
user=input("u want large number or small number 1\tsmaller\tlarger:: ")
if user=="larger":
    n=int(input(f"enter position upto {len(l1)}:: "))
    print(l1[-n])
else:
    n=int(input(f"enter position upto {len(l1)}:: "))
    print(l1[(n-1)])

print(l1)                                                                       