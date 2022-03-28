a=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d={}
for i in a:
    for j in a:
        if i[0]==j[0]:
           d.update({i[0]:[j[1],i[1]]})
           break
print(d) 

