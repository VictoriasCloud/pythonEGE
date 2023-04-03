letters='георий'
s=[]
k=0
for a in letters:
    for b in letters:
        for c in letters:
            for d in letters:
                for e in letters:
                    for f in letters:
                        for g in letters:
                            word=(a+b+c+d+e+f+g)
                            if word.count("г")==2 and word.count("е")==1 and word.count("о")==1 and word.count("р")==1 and word.count("и")==1 and word.count("й")==1:
                                k+=1
print(k)
