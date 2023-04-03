for R in range(0, 1000):
    N=bin(R)
    a=N.count("1")
    N=N+str(a%2)
    b=N.count("1")
    N=N+str(b%2)
    print(R, "--->", int(N,2))
