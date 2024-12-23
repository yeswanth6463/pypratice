# # count of prime num in given num 
# n=12498765431117
# strn=str(n)
# count = 0

# primary_set={'2','3','5','7'}

# for i in strn:
#     if i in primary_set:
#         count += 1
# print(count)

# n1=23456712738
# strn=str(n1)
# l=[]
# l.extend(strn)
# l1=max(l)
# print(l1)

#print n of prime number
n=20
l1=[]
count=0
i=2
while count<=n:
    f=0
    j=2
    while j<=i//2:
        if i%j==0:
            f+=1
            break
        j+=1
    if f==0:
      print(i)
      l1.append(i)
    count+=1
    i+=1
print(l1)
res=sum(l1)
print(res)
        