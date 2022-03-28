a={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
m,s,t=0,0,0
for i in a:
    for j in a:
        if a[j]>m:
            m=a[j]
        elif a[j]<m and a[j]>s:
            s=a[j]
        elif a[j]<s and a[j]>t:
            t=a[j]
print(m,"maximum")
print(s,"second max")
print(t,"third max")