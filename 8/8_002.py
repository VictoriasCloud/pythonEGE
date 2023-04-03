from itertools import*
d=[]
k=0
for i in product("лнос", repeat=4):
    #print(i)
    i="".join(i)
    k+=1
    #print(i)
    d.append(i)
    if k==249+1:
        print(i)
