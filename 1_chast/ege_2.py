print("x", 'y1', 'y2')
for x in (0,1):
    for y1 in (0,1):
        for y2 in (0,1):
            if ((((x, y1) and (x, y2))))==1:
                print(x, y1, y2)
