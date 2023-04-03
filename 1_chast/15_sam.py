def f(x, a1, a2):
    return ((a1<=x<=a2)<=((10<=x<=29)or(13<=x<=18)))
arr=[]
for a1 in range(0, 100):
    for a2 in range(0, 100):
        flag=1
        for x in range(0, 100):
            if f(x, a1, a2) == 0:
                flag = 0
                break
        if flag:
            arr.append(a2-a1)
arr.sort()
print(arr)
