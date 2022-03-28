# def key_having_similar_value(dic):
#     d={}
#     for i,j in dic.items():
#         d.setdefault(j,set()).add(i)
#     l=[j for i,j in d.items() if len(j)>1]
#     print(l)
# key_having_similar_value(dic={"age":23,"name":"onring","no.":23,"place":"navgurukul"})


dic={"a":20,"b":10,"c":20,"d":50,"e":20}
b=[]
for k,v in dic.items():
    for v1 in dic.values():
        if v == v1:
            v1=k
            b.append(v1)
        break
print(b)
