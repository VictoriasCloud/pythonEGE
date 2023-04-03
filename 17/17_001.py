s=[int(i) for i in open("17_rr.txt")]
#print(s)
count=0
maxim=0
for i in range(len(s)-1):
    for g in range(i+1, len(s)):
        if (s[i]+s[g])%9==0:
            count+=1
            maxim=max(maxim, (s[i]+s[g]))
print(count, maxim)


