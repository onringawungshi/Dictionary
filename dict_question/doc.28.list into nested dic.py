lis = [1, 2, 3, 4]
a={}
b={}
a=b
for i in lis:
    b[i] = {}
    b = b[i]
print(a)

