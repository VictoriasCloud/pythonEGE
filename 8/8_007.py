from itertools import*
k=0
for i in product("света", repeat=5):
    if i.count("с")>=1:
        k+=1
print(k)
