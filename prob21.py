def sum_divisors(i):
    """ find all the divisors of a number i and add 'em up """
    j = 1
    dl = []
    while j < i:
        if (i % j == 0):
            dl.append(j)
        j += 1
    return sum(dl)

# operates on a list of prime numbers --nope!
# file = open("primes_under_10000.txt","r")
# data = file.readlines()
# file.close()
# primes = [x.strip() for x in data[0].split(',')]
# for c in range(len(primes)):
#    primes[c] = int(primes[c])

tr = 10001 # top of range, plus one because it stops before this number

divisors = {}
temp = 0
for i in range(2,tr,1):
    divisors[i] = sum_divisors(i)

x = 0
y = 0
z = 0
amicables = 0

for i in range(2,tr,1):
    x = divisors[i]
    if x not in divisors: continue
    y = divisors[x]
    if y not in divisors: continue
    z = divisors[y]
    if z not in divisors: continue
    if divisors[z] == i and z != i:
        print(str(i) + " and " + str(divisors[i]))
        amicables += i

print(str(amicables))