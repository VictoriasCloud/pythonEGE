d="0123456789qwertyuhgfdsasdvbnbvcxz"
k=0
for i in range(13, 24):
    while i>0:
        if i%3==2:
            k+=1
        i=i//3
print(k)
