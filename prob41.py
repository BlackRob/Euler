import genPrimes


# warning, this is super slow, hours!
primes = genPrimes.genUpTo(1000000000)

def isPanDigital(x):
    """ x is an integer, which gets converted to a list of its digits,
        then the list is checked to see if it uses each of the digits
        from 1 to it's length once """
    y = [d for d in str(x)]
    xRef = ['1','2','3','4','5','6','7','8','9']  # [str(d) for d in range(1,len(y)+1)]
    for i in range(0,len(y)):
        if xRef[i] in y:
            pass
        else:
            return False
    return True

#print(len(primes))
#print(primes[-1])

for i in range(0,len(primes)):
    if isPanDigital(primes[i]):
        print(primes[i])