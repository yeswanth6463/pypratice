if __name__ == '__main__':
    l1=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l1.append([name,score])
    l2=[]
    for i in l1:
      for j in i:
        if isinstance(j,float):
            l2.append(j)
    # l3=min(l2)
    # for h in l2:
    #   if h==l3:
    #     l2.remove(h)
        
    # print(l2)
    # l4=min(l2)
    
    #second minimum    
    for k in l1:
      for s in k:
        if isinstance(s,float):
          if s==l4 :
            print(k[0])


