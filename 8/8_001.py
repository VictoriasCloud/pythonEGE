from itertools import*
d=[]
a="елмру"
k=0
for i in product(a, repeat=4):
    i="".join(i)
    k+=1
    d.append(i)
    if i[0]=="л":
        print(k, i, d.index(i)+1)
