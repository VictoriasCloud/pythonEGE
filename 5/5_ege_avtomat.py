for a in range(1,10):
    for b in range(0,10):
        for c in range(0,10):
            for d in range(0,10):
                for i in range(0,10):
                    #x=int(a)+int(b)+int(c)
                    #print(x)
                    f=a+int(c)+int(i)
                    #print(f)
                    g=int(b)+int(d)
                    #x=str(f)+str(g)
                    #y=str(g)+str(f)
                    #if x==723 or y==723:
                    #    print(a, b, c, d, y)

                    if int(f)>int(g):
                        h=int(str(g)+str(f))
                        #print(h)
                        if h==723:
                            print(a,b,c,d,i,"---НИКИТА ЛУЧШИЙ---",h)
                    else:
                        #print("   ХУЙНЯ    ")
                        s=int(str(f)+str(g))
                        if s==723:
                            print(a,b,c,d,i,"---НУ НИКИТА РЕАЛЬНО КРАСАВЧИК---", s)
                        ##if len(str(h))==3:
                            #print(h)
                        #if s==723:
                            #print(s)
