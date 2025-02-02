import json

data = '{"name":"yeswanth","age":"22","degree":"B.Tech","percentage":"84%","contact":{"email":"yeswanth6463@gmail.com","phno":"9597470128"},"address":"vellore"}'
print(type(data))  # Should print: <class 'str'>
res = json.loads(data)
print(type(res))  # Should print: <class 'dict'>

res2=json.dumps(data)
print(type(res2))  # Should print: <class 'str'>

with open('inde2x.json','w') as fh :
    if fh.writable():
        json.dump(res2,fh)
        print("data dumped")
    