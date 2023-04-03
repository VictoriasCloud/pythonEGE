from itertools import permutations
k=0
c=0
for i in permutations("руслан"):
    i="".join(i)
    k+=1
    if ("уа" not in i) and ("ау" not in i):
        c+=1
        print(i)
print(c,k)
