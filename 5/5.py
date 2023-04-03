for i in range(1, 1000):
    N=(bin(i)[2:])
    c=N.count('1')%2
    n=N+str(c)
    a=n.count('1')%2
    b=n+str(a)
    print(i, b, (int(b, 2)))

