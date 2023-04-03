def f(a, x, y):
    return (((y+2*x)!=48)or(a<x)or(a<y))

for a in range(1, 500):
    flag=1
    for x in range(1, 500):
        for y in range(1, 500):
            if f(a, x, y)==0:
                flag=0
    if flag==1:
        print(a)

