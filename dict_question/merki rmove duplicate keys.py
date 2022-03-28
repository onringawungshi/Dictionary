dic={"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3}
dic1={}
list1=[]
for i,j in dic.items():
    if j not in list1:
        list1.append(j)
        dic1[i]=j
print(dic1)