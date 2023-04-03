s="1"+"9"*100
#print(s)
while "19" or "299" or "3999" in s:
    s=s.replace("19", "2", 1)
    s=s.replace("299","3", 1)
    s=s.replace("3999","1", 1)

    print(s)

