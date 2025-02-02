# # e element same order if it is same elements present in list 1 in same order p
# l1 = [1, 2, 3, 4,6,5, 7]
# l2 = [4,5]
# r=" "
# for i in range(len(l1)-1):
#     if l1[i]==l2[0] and l1[i+1]==l2[1]:
#           r=True
# if bool(r)==True:
#     print("true")
# else:
#     print("false")

 
# #can u find list 2 element is present and same order in list 1 if it is same true else false
# print(set(l1) & set(l2))
# if set(l1) & set(l2)
#     print("True")
# else:
#     print("False") 
# print(l1[3:3+len(l2)])
   

def is_adjacent(l1, l2):
    # Check if sublist appears as a consecutive sequence in mainlist
    for i in range(len(l1) - len(l2) + 1):
        if l1[i:i + len(l2)] == l2:
            return True
    return False
# Check if elements 4 and 5 are adjacent in list1
result = is_adjacent(l1, l2)
pr                         int(result)

# # def flatten(val):
# #     l1 = []
# #     for i in val:
# #         if isinstance(i, list):
# #             l1.extend(flatten(i))  
# #         else:
# #             l1.append(i) 
# #     return l1

# lis = [10, 20, [20, 50, [6, 7]], 100, [5, [6, 7, 8]]]

# def flat(val):
#     l1=[]
#     for i in val:
#         if isinstance(i,list):
#             l1.extend(flat(i))
#         else:
#             l1.append(i)
#     return l1
# flat(lis)
# print(flat(lis))
            
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
    l3=sorted(set(i for i in l2))
    l5=[l3]
    l3.remove(1)
    l4=min(l3)
    
    #second minimum    
    for k in l1:
      for s in k:
        if isinstance(s,float):
          if s==l4 :
            print(k[0])











# flatten(lis)
# print(flatten(lis))

# l1=[2,3,4,5,6,[45,67,89,78],[79,30,20,[560,708,[897,786,[45567,786940]]]]]
# l2=[]
# for i in l1:   
#    def flat(val):
#     l1=[]
#     for i in val:
#         if isinstance(i, list):
#             l1.extend(flat(i))
#         else:
#             l1.append(i)
#     return l1
# print(flat(l1))



####
# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n + fact(n-1)
    
# print(fact(5))



