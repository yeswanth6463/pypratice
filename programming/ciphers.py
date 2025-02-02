st1="yeswanthz"
res=""
for i in st1:
    if i in 'Z':
        res+=chr(65)
    elif i in 'z':
        r=chr(97)
        res+=r
    else:
        res+=chr(ord(i)+1)
print(res)