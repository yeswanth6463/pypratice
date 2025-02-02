words=['listen','silent','enlist','rat','art','tar','bog','god']

res={}

for i in words:
    s=tuple(sorted(i))
    if s in res:
        res[s].append(i)
        print(res[s])
    else:
        res[s]=[i]
    l=list(res.values())
print(l)