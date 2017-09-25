import pickle

with open("primes.pickle", "rb") as fp: 
    primes = pickle.load(fp)

s = len(primes)

for i in range(s-1):
    if primes[i] < primes[i+1]:
        pass
    else:
        print(primes[i],primes[i+1],i)
