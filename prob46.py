import genPrimes
import math

def genSquares2(x):
    squares2 = []
    i = 1
    while i <= x:
        squares2.append(2*i*i)
        i = i + 1
    return squares2

def main():
    maxNum = 10000
    maxNumSQRT = math.ceil(math.sqrt(maxNum))
    primes = genPrimes.genUpTo(maxNum * 2)
    squares2 = genSquares2(maxNumSQRT)
    oddComposites = []
    j = 3
    while j <= maxNum:
        if j not in primes:
            oddComposites.append(j)
        j += 2

    print(oddComposites)
    #print(primes)
    print(squares2)

    for oddComp in oddComposites:
        k = 0   # counter for primes list
        l = 0   # counter for squares list
        oddCompMinusPrime = 0
        found = False    # if we found a way to make the composite number  
        while k < len(primes) and not found:
            oddCompMinusPrime = oddComp - primes[k]
            if oddCompMinusPrime < 0:
                break
            found = oddCompMinusPrime in squares2
            #if found:
             #   squares2.index(oddCompMinusPrime)
              #  print("found:",oddComp," minus ",primes[k], "=",oddCompMinusPrime)
            k += 1
        
        if not found:
            print("Not found:", oddComp)
                # break
                

if __name__ == '__main__':
  main()