# l1=['S001', 'S002', 'S003', 'S004']
# l2=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# l3=[85, 98, 89, 92]
# d={}
# k=0
# for i in l1:
#     for j in l2:
#         d[i]={}
#         d[i][j]=l3[k]
# print(d)
    
a=[1,2,3]
b=["a","b","c"]
d={}
for i in a:
    for j in b:
        d[i]=j
        b.remove(j)
        break
print(d)

f = open("hobby.txt","w")
h = [ ]
for i in range(5):
       n = input("Enter hobby name")
       h.append(n,'\n')
f.writelines(h)
f.close()