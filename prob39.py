import math

squares = [0]

for a in range(3, 500):
    for b in range(a, 500-a):
        c = math.sqrt(a*a + b*b)
        if (c%1 != 0):
            continue
        c = int(c)
        p = a+b+c
        if (p <= 1000):
            squares.append(p)
            #print(a,b,c,p)

#print(squares)

perimetersDict = dict()
for i in squares:
    if i in perimetersDict:
        perimetersDict[i] += 1
    else:
        perimetersDict[i] = 1

maxP = max(perimetersDict.values())
maxInDict = {k:v for (k,v) in perimetersDict.items() if (v==maxP)}
print(maxInDict)

