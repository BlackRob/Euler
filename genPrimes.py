import math


# not very efficient, should improve  :)
def genUpTo(x):
    found = [2,3]
    i = 5
    while i <= x:
        r = math.ceil(math.sqrt(i))
        j = 1
        while j <= len(found):
            if i % found[j] == 0:
                break
            if found[j] < r:
                j += 1
                continue
            found.append(i)
            break
        i += 2 
    return found

# print(genUpTo(100000))