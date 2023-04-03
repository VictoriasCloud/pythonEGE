def f(s, c):
    while s>0:
        if s%6==5:
            c+=1
        s=s//6
    return c
for i in range(1, 1000):
    x=i
    c=0
    s=216**5 +6**3 -1 - x
    if f(s, c)==12:
        print(i)#259

