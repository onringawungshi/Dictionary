d={'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 150, 'g': 57, 'h': 8, 'l': 100}
a=[]
for i,j in d.items():
    a.append(j)
    a.sort()
    b=a[-1]
    b=i
    print(b)
    
    