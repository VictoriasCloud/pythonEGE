for i in range(1, 500):
    x=i
    s=216**5 +6**3-1 - x
    c=0
    while s>0:
        if s%6==5:
            c+=1
        s=s//6
    if c==12:
        print(x)

