a={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
b=[]
d={}
for i in a:
    for j in a[i]:
        if type(j)==type([]):
            j=str(j)
        d.update({i:j})
print([d])