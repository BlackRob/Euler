def sum_divisors(i):
    """ find all the divisors of a number i and add 'em up """
    j = 1
    dl = []
    while j < i:
        if (i % j == 0):
            dl.append(j)
        j += 1
    return sum(dl)

""" problem states we need to find all the abundant numbers in a specific range
(up to tr), so owe have to find the sum of divisors for all the numbers in that 
range, then see which ones are abundant """

tr        = 28123 # top of range
divisors  = {}
abundants = []

for i in range(2,tr+1):
    divisors[i] = sum_divisors(i)
    if divisors[i] > i and divisors[i] < tr:
        # abundants[i] = divisors[i] # abundants is now a list, not a dict
        abundants.append(i)
        # print(str(i), ' ', abundants[i]) #tested, dict of abundants works
        # print(i)

""" next have to have a list of all ints up to tr, then eliminate every one that 
is the sum of two abundant numbers """

abunsize = len(abundants)
allints = list(range(1,tr+1))

for i in range(abunsize):
    for j in range(i,abunsize):
        x = abundants[i] + abundants[j]
        if x in allints:
            allints.remove(x)
        if x > tr: continue

print(sum(allints))