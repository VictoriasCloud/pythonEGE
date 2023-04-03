from itertools import*
s=[]
for i in product("икн", repeat=2):
    i="".join(i)
    s.append(i)
b=(len(s))
from itertools import*
s=[]
for i in product("икн", repeat=3):
    i="".join(i)
    s.append(i)
c=(len(s))
from itertools import*
s=[]
for i in product("икн", repeat=4):
    i="".join(i)
    s.append(i)
l=(len(s))
print(l+c+b)
