if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    l1=[]
    for i in range(n+x):
        for j in range(n+y):
            for k in range(n+z):
                l1.append([i,j,k])
    l2=[]            
    for s in l1:                
      if sum(s)!=n:
        l2.append(s)
print(l2)

