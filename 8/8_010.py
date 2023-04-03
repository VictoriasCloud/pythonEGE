from itertools import*
c=0
for i in product("012345678", repeat=5):
    i="".join(i)
    if i.count("5")==1 and i[0]!="0":
        if i[-1]=="5":
            if ((i[3]))not in "1234":
                c+=1
        elif i[0]=="5":
            if ((i[1])) not in "1234":
                c+=1
        else:
            if (((str(i[(i.index("5")+1)])) not in "1234") and ((str(i[(i.index("5")-1)])) not in "1234")):
                c+=1
print(c)
