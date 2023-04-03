s = 1000*"8"
#print(s)
while "999" in s or "888" in s:
    if "999" in s:
        s=s.replace("999", "88", 1)
    if "888" in s:
        s=s.replace('888', '9', 1)
print(s)
#s=s[:-1]
#print(sum(list(map(int, s))))
