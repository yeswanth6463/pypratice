try:
    with open("notes.txt",'r') as fh:
        if fh.readable():
            print("File is readable")
            d=fh.read().split()
            # print(d)
            t=0
            for i in d:
                if '0'<=i<='9':
                    t+=int(i)
        print(t)
                    
except FileNotFoundError as fe:
    print(fe)