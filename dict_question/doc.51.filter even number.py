# a={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
a={'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
b={}
for i in a:
    c=[]
    for j in a[i]:
        if j%2==0:
            c.append(j)
        b.update({i:c})
print(b)