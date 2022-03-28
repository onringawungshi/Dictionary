# a={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# d=[]
# b={}
# for key,value in a.items():
#     for i in value:
#         b.update({key:i})
#         d.append(b)
#     print(d)
#     break

d={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
c=result = map(dict, zip(*[[(key, val) for val in value] for key, value in d.items()]))
print(list(c))