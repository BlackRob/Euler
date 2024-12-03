import genPrimes
import math

def distinctFactors(factors: list):
   df = []
   for n in factors:
      if n in df:
         continue
      else:
         df.append(n)
   #print(factors,df,len(df))
   return len(df)

def main():
    maxNum = 1000000
    primes = genPrimes.genUpTo(maxNum)
    
    #print(primes)

    i = 2   # initial value
    j = 0   # muteable version of i
    in_a_row = 0
    factors = []
    while i <= primes[-1]:
        factors = []
        if i in primes:
            i += 1
            in_a_row = 0
        else:
            j = i
            k = 0
            while j > 1:
                rem = j % primes[k]
                if  rem == 0:
                    factors.append(primes[k])
                    j = int(j / primes[k])
                else:
                    k += 1
            df = distinctFactors(factors)
            if df == 4:
                #print(i,"has",df,"factors,",factors)
                in_a_row += 1
            else: 
                in_a_row = 0
            if in_a_row == 4:
                print("4 in a row, ending on",i)
                in_a_row = 0
                break
            i += 1

            

if __name__ == '__main__':
  main()