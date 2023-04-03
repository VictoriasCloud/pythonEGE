for a in range(1,10):
    for b, c, d, i in range(0,10):
        f=a+c+i
        g=b+d
        if int(f)>int(g):
            h=int(str(g)+str(f))
            if h==723:
                print(a,b,c,d,i,"---НИКИТА ЛУЧШИЙ---",h)
        else:
            s=int(str(f)+str(g))
            if s==723:
                print(a,b,c,d,i,"---НУ НИКИТА РЕАЛЬНО КРАСАВЧИК---", s)
