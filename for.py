for i in range(1,6,2):
    for j in range(1,4):
        if i==4:
            break
        print(i,end="")
    print()

t1=(10,20,30,40,50,60,70,80,90)

for i in t1:
    for j in range(1,4):
        if i==60:
            continue
        print(i,end=" ")
    print()
        
#remove duplicate
t1=(10,20,30,40,50,60,60)
for i in t1:
    for j in range(1,5):
        print(i,end=" ")
    print()
        
    
    


