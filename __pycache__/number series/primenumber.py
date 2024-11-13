def n_of_primenum(n):
    count=0
    i=2
    l=[]
    while count<n:
        f=0
        j=2
        while j<=i//2:
            if i%j==0:
                f+=1
                break
            j+=1
        if f==0:
            l.append(i)
            count+= 1
        i+= 1
    return f"{l}"
res=n_of_primenum(n=int(input("n::")))

print(res)

n=int(input("n::"))

for i in range(2,n+1):
    f=0
    for j in range(2,i//2+1):
        if i%j==0:
            f+=1
            break
    if f==0:
        print(i,end=" ")
print()
        
# #lcm
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

m = max(n1, n2)
while True:
    if m % n1 == 0 and m % n2 == 0:
        break
    m += 1

print(m, end=" ")

for i in range(m,(n1*n2)+1):
    if i%n1==0 and i%n2==0:
        print(i,end=" ")
        break
    
