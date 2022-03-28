my_dict = {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
x=0
y=0
z=0
a=[]
for i in my_dict:
    for j in my_dict.values():
        if j>x:
            x=my_dict[i]
            b=i
        elif j<x and j>y:
            y=my_dict[i]
            c=i
        elif j<y and j>z:
            z=my_dict[i]
            d=i
a.append(b)
a.append(c)
a.append(d)
print(a)
