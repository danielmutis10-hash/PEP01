(w,x,y,z) = (0,0,0,0)

for x in range(11):
    if (x % 2 == 0):
        print(x)

for y in range (11):
    if (y % 2 != 0 ):
        continue
    print(y)

while (w != 11):
    if (w % 2 == 0):
        print(w)

    w+=1

while (z != 11):
    if (z % 2 !=0):
        z += 1
        continue
    print(z)
    z += 1