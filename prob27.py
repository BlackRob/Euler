# import a list of prime numbers
file = open("primes_under_10000.txt","r")
data = file.readlines()
file.close()
primes = [x.strip() for x in data[0].split(',')]
for c in range(len(primes)):
    primes[c] = int(primes[c])

print(str(primes[-1]))

# ranges for the coefficients in our quadratic equation
arange = range(-999,1000)
brange = range(-1000,1001)

n = 0
candi = 2
longStreak = 0
lStreakProd = 0

for a in arange:
    for b in brange:
        n = 0
        candi = 2
        while candi in primes:
            candi = n**2 + a*n + b
            if candi > 9973:
                print(candi,"We need more primes")
            if candi in primes:
                n += 1
            else:
                if n > longStreak:
                    longStreak = n
                    lStreakProd = a * b
                    print('a',a,'b',b,longStreak)
                break

print(longStreak)
print(lStreakProd)
                    
                