for i in range(0,100):
    N=bin(i)[2:]
    k=N.count("1")
    N+=str(k%2)
    x=N.count("1")
    N+=str(x%2)
    print(i,"=>",int(N,2))
