s="123.15.167.550"
l=s.split(".")
f=True
# def isdigit2(r):
#     for i in l:
#         if "0"<=i<="9":
#             return True
#         else:
#             return False
c=len(l)
if c==4:
    for i in l:
        if i.isdigit() and 0<=int(i)<=255 :
            f=True
        else:
            f=False
            break
else:
    print("not valid")
if f==True:
    print("valid")
else:
    print("not valid")
# for i in s:
    # l+=i
    # if i==".":
    #     count+=1
    #     print(l)
    #     if count>3:
    #         print("it is not a valid ip address")
    #         break
       