# s="csk rcb mi"
# v=""
# for i in s:
#     if i.isalpha():
#         v+=i
# rev=v[::-1]
# print(rev)
# res=""
# for i in len(s):
#     if s[]!=" " and s[i]==" ":
#         rev+=i


#consicute two string:
# s="abcd"
# r="abc"
# def checkstr(s,r):
#     for i in range(len(s)-len(r)+1):
#         if s[i:i+len(r)]==r:  
#             return True
#     return False

# res=checkstr(s,r)
# print(res)  
# if res==True:
#     print("conscutively present")
# else:
#     print("not present")         
# s="csk rcb mi"
# w=s.split()
# rev=[w[::-1] for i in w]
# ro=[rev[-1]]+rev[:-1]
# op=" ".join(ro)
# print(op)
# 
# s="csk vs mi,match draw csk win and ruthuraj is man of the match"
# l=[]
# r=""
# for i  in s:
#     if i!=" " and i!=",":
#         r+=i
#     else:
#         if r!="":
#          l.append(r)
#          r=""
# if r!="":
#     l.append(r)
# print(l)
# d=""
# for i in l:
#     if len(i)>len(d):
#         d=i
# print(d)

s = "aabbaaaafff"
rs = ""
c = 1  

for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        c += 1
    else:
        rs += s[i] + str(c)
        c = 1  
rs += s[-1] + str(c)

print(rs)

str='csk rcb mi'
l=list(str.replace(" ",""))
r=""
for i in str:
    if i!=" ":
        a=l.pop()
        r+=a
    else:
        r+=' '
print(r)





        
        
        
        



# l2=[]
# for i in l:
#     l2.append(len(i))
# ma=max(l2)
# pos=l2.index(ma)
# print(l[pos])

