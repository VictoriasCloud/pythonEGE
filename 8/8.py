from itertools import *
d="иван"
count=0
for i in product(d, repeat=5):
    if i.count("и")>=1:
        count+=1
print(count)
