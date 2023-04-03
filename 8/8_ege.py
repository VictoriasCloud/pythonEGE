letters='АКО'
s=[]
for a in letters:
    for b in letters:
        for c in letters:
            for d in letters:
                for i in letters:
                    s.append(a+b+c+d+i)
print(s.index('ООАОО')+1)
