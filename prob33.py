# digit cancelling fractions

def compare(i,j,k,l):
    """ compare fractions i/j and k/l to see if they are equivalent """
    if i*l == j*k:
        return True
    else:
        return False

dcf = {}
dcf2 = {}
numProd = 1
denProd = 1

for i in range(11,99):
    for j in range(i+1,100):
        if j % 10 == 0 and i % 10 == 0:
            continue
        numDigits = [int(d) for d in str(i)]
        denDigits = [int(d) for d in str(j)]
        for k in numDigits:
            if k in denDigits:
                numDigits.remove(k)
                denDigits.remove(k)
                if compare(i,j,numDigits[0],denDigits[0]):
                    dcf[i] = j
                    dcf2[numDigits[0]] = denDigits[0]
                    print(numDigits[0],denDigits[0])
                    numProd *= numDigits[0]
                    denProd *= denDigits[0]

print(dcf)
print(dcf2)
print(numProd,denProd)
