a={"a":12,"b":15,"c":20,"d":8,"f":3}
s={}
b=sorted(a.values())
for i in b:
    for k in a.keys():
        if a[k] == i:
            s[k] = a[k]
            break

print(s)
