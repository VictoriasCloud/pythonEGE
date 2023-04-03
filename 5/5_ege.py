for i in range(1000, 10000):
    one=int(str(i)[0])+int(str(i)[1])
    #print(one)
    two=int(str(i)[1])+int(str(i)[2])
    three=int(str(i)[2])+int(str(i)[3])
    a=sorted([one, two, three], reverse=1)
    r=str(a[1])+str(a[0])
    if r=="1517":
        print(i)
    #print(a, r)
