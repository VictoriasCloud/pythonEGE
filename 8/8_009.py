from itertools import*
d=[]
for i in product("алпця", repeat=5):
    i="".join(i)
    d.append(i)
    if i.count("а")<=1 and i.count("ц")==2 and i.count("л")==0:
        print(d.index(i)+1, i)
