def f(a, x):
    return (((x in a)<=(x in p))or((x not in q)<=(x not in a)))
p=[i for i in range(2, 21, 2)]
q=[i for i in range(3, 31, 3)]

a=set([i for i in range(1,50)])
for x in [i for i in range(1,50)]:
    if f(a,x)==0:
        a.remove(x)
print((sorted(a)))

