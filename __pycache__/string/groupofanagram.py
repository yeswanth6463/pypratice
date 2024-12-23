l=["listen","silent","enlist","art","tar","rat","dog","god"]
# l3=[]
# for i in l:
#     l1=[]
#     l3.append(l1)
#     for j in i:
#         l1.append(j)
# l4=[]
# for i in l3:
#     i.sort()            
#     l4.append(i)
# d={k:v for k,v in zip(l,l4)}
# l6 = []
# used = set()
# for key, value in d.items():
#     if key not in used:
#         l5 = []
#         for k, v in d.items():
#             if v == value:
#                 l5.append(k)
#                 used.add(k)
#         l6.append(l5)

# print(l6)

ar={}
for i in l:
    s=tuple(sorted(i))
    if s in ar:
        ar[s].append(i)
    else:
        ar[s]=[i]
l=list(ar.values())
print(l)