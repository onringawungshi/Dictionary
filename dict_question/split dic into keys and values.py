def different_list(dic):
    keys=[]
    values=[]
    for i,j in dic.items():
        keys.append(i)
        values.append(j)
    print(keys)
    print(values)
different_list({"age":23,"name":"onring","place":"bangalore"})