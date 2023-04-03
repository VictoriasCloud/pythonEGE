from itertools import*
k=0
for i in product("аегц", repeat=5):
    k+=1
print(k, 4096+1024)
