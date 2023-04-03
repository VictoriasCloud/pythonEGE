for i in range(10000,100000):
    spisok=list()
    i=str(i)
    a=int(i[0])+int(i[2])+int(i[4])
    b=int(i[1])+int(i[3])
    spisok.append(a)
    spisok.append(b)
    #print(spisok)
    spisok=sorted(spisok)
    if "".join(map(str, spisok))=="723":
        print(i)
