letters="АОУ"
s=[]
for a in letters:
    for b in letters:
        for c in letters:
            for e in letters:
                for f in letters:
                    s.append(a+b+c+e+f)
print(s[100])
