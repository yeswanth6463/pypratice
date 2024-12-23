

    

# r=int(input("enter a row "))
# c= int(input("enter a column "))
# # res=[[int(input(f"value {i} ,{j}:")) for j in range(c)]for i in range(r)]
# # print(res)
# m1=[[int(input(f"enter a {i},{j} input")) for j in range(c)] for i in range(r) ]
# m2=[[int(input(f"enter a {i},{j}  input")) for j in range(c)] for i in range(r) ]
# res =[[0 for j in range(c)]for i in range(r)]
# res2 =[[0 for j in range(c)]for i in range(r)]
# res3 =[[0 for j in range(c)]for i in range(r)]

# print(res)
# for i in range(r):
#     for j in range(c):
#         res[i][j]=m1[i][j]+m2[i][j]
#         res2[i][j]=m1[i][j]-m2[i][j]       
#         res3[i][j]=m1[i][j]*m2[i][j]       
# print(res)
# print(res2)
# # print(res3)p                       0

# r=int(input("enter a row "))
# c= int(input("enter a column "))
# res=0
# m1=[[int(input(f"enter a {i},{j} input")) for j in range(c)] for i in range(r) ]
# m2=[[int(input(f"enter a {i},{j}  input")) for j in range(c)] for i in range(r) ]
# res=[[int(input( "enter the res:" )) for i in range(c) for i in range(r)]]
# res=[0]
# for i in range(r):
#     for j in range(c):
#         for k in range(r):
#             m1[i][j]*m2[i][j]
# print(m1)
#matrix multiplication
# m1=[[1,2,3],[4,5,6],[7,8,
# 9]]
# m2=[[9,8,7],[6,5,4],[3,2,
# 1]]
# res=[[0 for j in range(3)]for i in range(3)]
# for i in range(3):
#     for j in range(3):
#         for k in range(3):
#             res[i][j]+=m1[i][k]*m2[k][j]
# print(res)
r=int(input(" r :"))
c=int(input(" C: "))
m1=[[int(input(f" valuek {i} {j} :")) for j in range(c)] for i in range(r)]
r1=int(input(" r :"))
c1=int(input(" C: "))
m2=[[int(input(f" value {i} {j} :")) for j in range(c1)] for i in range(r1)]                                                                                                                                                                
res=[[0 for j in range(c1)] for i in range(r)]
# print(m1)
# print(m2)
for i in range(len(m1)):
         for j in range(len(m2[0])):
             for k in range(len(m2)):
                #  print(f"{i},{j},{k} ",end=" ")
                 res[i][j]+=m1[i][k]*m2[k][j]

                # for k in range(len(m1[0])):
                #     res[i][j]=m1[i][j]*m2[i][j]

print(res)
        
                