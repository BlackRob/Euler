import sys

def triCalc (n: int):
    return int((n*(n+1))/2)

def pentCalc (n: int):
    return int((n*(3*n-1))/2)

def hexCalc (n: int):
    return int((n*(2*n-1)))

def main():
    #x: int = 8
    trinums: list = []
    pentanums: list = []
    hexanums: list = []

    isInPentanums: bool
    isInHexanums: bool
    
    for i in range(1,100000):
        isInPentanums = isInHexanums = False
        # calculate the i th number of each type
        # and add each number to proper list
        trinums.append(triCalc(i))
        pentanums.append(pentCalc(i))
        hexanums.append(hexCalc(i))
        isInPentanums = trinums[i-1] in pentanums
        isInHexanums = trinums[i-1] in hexanums

        #print(trinums[i-1],pentanums[i-1],hexanums[i-1])
        
        # check if trinum is also in pentanums list
        if isInPentanums:
            print("___",trinums[i-1], "is in pentanums at ", pentanums.index(trinums[i -1])+1)
            if isInHexanums:
                print("_______",trinums[i-1], "is in hexanums at ", hexanums.index(trinums[i -1])+1)
        

if __name__ == '__main__':
  main()