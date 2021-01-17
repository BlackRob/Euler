def isPanDigital(x):
    """ x is a 9 character string, which gets converted to a list of its digits,
        then the list is checked to see if it uses each of the digits 1-9 """
    
    y = [d for d in x]
    xRef = ["1","2","3","4","5","6","7","8","9"]
    for i in range(9):
        if xRef[i] in y:
            pass
        else:
            return False
    return True

cp = [] #concatenated products

for i in range(1,10000):
    x = i
    tcp = ""
    for j in range(1,10):
        y = j*x
        tcp += str(y)
        if (len(tcp) == 9):
            if (isPanDigital(tcp)):
                print(i," ",tcp)
                cp.append(int(tcp))
        if (len(tcp) > 9):
            pass

print(cp)
print("max = " + str(max(cp)))