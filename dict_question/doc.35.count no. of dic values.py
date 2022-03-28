def count_value(dic):
    c=0
    for i,r in dic.items():
        for j in dic[i]:
            c=c+1
    print(c)
count_value({'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']})