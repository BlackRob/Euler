import pickle

with open("primes.pickle", "rb") as fp: 
    primes = pickle.load(fp)

def rotate(integer):
    """ rotate takes a positive integer and returns a list containing that
    integer and every rotation of its digits, i.e. 123, 231, 312 """
    x = []
    s = len(str(integer))
    magni = (10 ** (s-1))
    for j in range(s):
        x.append(integer)
        integer = (integer%magni)*10 + integer//magni
    return x
    
def isCircular(alist):
    """ checks if every number in the rotated list is prime """
    global primes
    for j in alist:
        if j not in primes:
            return False
    return True

counter = 0

for i in primes:
    x = rotate(i);
    if isCircular(x):
        print(x)
        counter += 1
    
print(counter)