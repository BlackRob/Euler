# pandigital numbers!

def isPanDigital(x):
    """ x is an integer, which gets converted to a list of its digits,
        then the list is checked to see if it uses each of the digits 1-9
        once and only once """
    if (len(str(x))) != 9:
        return False
    
    y = [int(d) for d in str(x)]
    xRef = [1,2,3,4,5,6,7,8,9]
    for i in range(0,9):
        if xRef[i] in y:
            pass
        else:
            return False
    return True


pandiProducts = []

for i in range(1,10000):
    for j in range(1,10000):
        x = i*j
        xStr = str(i) + str(j) + str(x)
        if (isPanDigital(xStr)):
            print(i,'x',j,'=',x)
            if x not in pandiProducts:
                pandiProducts.append(x)


print(pandiProducts)
print(sum(pandiProducts))