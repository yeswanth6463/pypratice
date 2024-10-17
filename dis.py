###########################################################
a =int(input("a:"))
b = int(input("b:"))
a=a^b
b=a^b
a=b^a
print(f"a:{a}")
print(f"b:{b}")

#######################table##############################
n=int(input("enter a num: "))
up=int(input("upto :"))
for i in range(1,up+1):
    print(f"{n}*{i}={n*i}")
###########################################################
for s in range(5,-6,-1):
    print(s,end=" ")