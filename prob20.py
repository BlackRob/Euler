from math import factorial

n = 1

while n < 100:
    n += 1
    nfac_string = str(factorial(n))
    nfac_sum = 0
    for c in nfac_string:
        nfac_sum = nfac_sum + int(c)
    print( str(n) + ' ' + nfac_string + ' ' + str(nfac_sum))

    