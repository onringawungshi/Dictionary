# a=[1000,27,345,12345,201]
# c=[]
# i=0
# while i <len(a):
#     b=str(a[i])
#     b=list(b)
#     b.pop()
#     c.append(b)
#     i+=1
# d=[]
# j=0
# while j<len(c):
#     f="".join(c[j])
#     d.append(int(f))
#     j+=1
# print(d)

d = { 'a': 1, 'b': 2, 'c': 3 }
a=list(map(list, d.items()))
print(a)