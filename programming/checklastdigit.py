l=[123,44434,21343,453]
l2=[]
for i in l:
    rem=i%10
    l2.append(rem)
    
for i in range(len(l2)-1):
    if l2[i]==l2[i+1]:
        print(True)
        break
    else:
        print(False)
        break
    
    
