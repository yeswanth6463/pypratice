l=[10,20,'hello','10',17.6]
# s=0
# for i in l:
#     if type:()
#         s+=l
        
# print(s)

l1=[i for i in l  if type(i)==int ]
print(sum(l1))


t1=sum(i for i in l if type(i)==int)

print(t1)



s=sum(i for i in l if isinstance(i,(int,float)))
print(s)


n=[10,20,50.55,"hello",(1+6j)]
c=d=e=f=g=0


for i in n:
    if type(i)==int:
        c+=1
    if type(i)==float:
        d+=1
    if type(i)==complex:
        e=+1
    if type(i)==str:
        f+=1
    if type(i)==bool:
        g+=1
    
print(f"int :{c}")
print(f"float :{d}")
print(f"complex:{e}")
print(f"str :{f}")
print(f"bool:{g}")