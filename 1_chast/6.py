for i in range(1, 100000):
    x=i
    s=x
    s = s // 10
    n = 1
    while s < 221:
        if n % 2 == 0:
            s = s + 13
        n = n + 5
    if n==121:
        print(x)
