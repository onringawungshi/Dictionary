dic={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
a=sorted(dic.values())
b={}
for i in a:
    for j in dic.keys():
        if dic[j]==i:
            b[j]=dic[j]
print(b)