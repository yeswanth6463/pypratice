# def index_grid(rows,columns):
#     d1=[]
#     for i in range(rows):
#         d=[]
#         for j in range(columns):
#             d.append((i,j))
        
#         d1.append(d)
#     return d1
    
# res=index_grid(4,3)
# print(res)



str='Aes34@!nid*&bbd895@@42'
c=0
for i in str:
    sr="+-*/|_(}{)'~`><,.%$#@!;:"
    if i in sr:
        c+=1
        
print(c)
if c%2==0:
    for i in str:
        if i.isalnum():
            print(i,end='')
            
else:
    for i in str:
        if '0'<=i<='9':
            if int(i)%2==1:
                