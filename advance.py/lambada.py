name=['Captain America','Dead Pool','Iron Man','Bat Man']
def capts(name):
    r=[]
    for i in name:
        res=''.join([word[0] for word in i .split()])
        r.append(res)
    return r
    

print(capts(name))

capts(name)
print(list(map(lambda data:"".join([word[0] for word in data .split()]),name)))


p=[102,235,1034,965,456,745]

print(list(map(lambda data:data-(data//100)*5,p)))