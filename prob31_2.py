""" we will keep a list of all combinations as strings, coded into letters
    and sorted alphabetically so they can be compared, so the same
    combination doesn't appear twice, even if it is generated twice
    200 => 'h'
    100 => 'g'
    50 => 'f'
    20 => 'e'
    10 => 'd'
    5 => 'c'
    2 => 'b'
    1 => 'a'    """ 
    
cv = {'a':1, 'b':2, 'c':5, 'd':10, 'e':20, 'f':50, 'g':100, 'h':200}

def addToCombos(newCombo):
    global combos
    if newCombo not in combos:
        combos.append(newCombo)

def swapIt(chRemove,chReplace,aList):
    check = aList.count(chRemove)
    if check >= cv[chReplace]:
        temp = list(aList)
        for i in range(chValue):
            temp.remove(chRemove)
        temp.append(chReplace)
        temp.sort()
        addToCombos(str(temp))
        if 'h' not in temp:
            transform(temp)


def transform(someList):
    swapIt('a','h',someList)
    swapIt('a','g',someList)
    swapIt('a','f',someList)
    swapIt('a','e',someList)
    swapIt('a','d',someList)
    swapIt('a','c',someList)
    swapIt('a','b',someList)
    swapIt('b','h',someList)
    swapIt('b','g',someList)
    swapIt('b','f',someList)
    swapIt('b','e',someList)
    swapIt('b','d',someList)
    swapIt('b','c',someList)
    swapIt('c','h',someList)
    swapIt('c','h',someList)
    swapIt('c','h',someList)
    swapIt('a','h',someList)
    swapIt('a','h',someList)
    swapIt('a','h',someList)
    swapIt('a','h',someList)
    swapIt('a','h',someList)
    swapIt('a','h',someList)
"""    checkA = someList.count('a')
    if checkA >= 200:
        temp = list(someList)
        for i in range(200):
            temp.remove('a')
        temp.append('h')
        temp.sort()
        addToCombos(str(temp))
        if 'h' not in temp:
            transform(temp)
    if checkA >= 100:
        temp = list(someList)
        for i in range(100):
            temp.remove('a')
        temp.append('g')
        temp.sort()
        addToCombos(str(temp))
        if 'h' not in temp:
            transform(temp)
    if checkA >= 50:
        temp = list(someList)
        for i in range(50):
            temp.remove('a')
        temp.append('f')
        temp.sort()
        addToCombos(str(temp))
        if 'h' not in temp:
            transform(temp)
   """     

"""
    we start with a list representing a combination made of just
    the smallest coins, 200 1 pence coins; every combination must be different
    from every other combination by at least one coin transformation (two 1p to
    one 2p, or ten 1p to two 5p)
    
    we take that list and ask, what are all of the single transformations we
    could make, then we make each change to a copy of the list
    
    every change means a new combo: for each new combo we sort it, turn
    it into a string, and check it against our list of previously generated
    combinations; if it's unique, we add it to the list
    
    after every transformation, we recursively do this again on a copy of
    the transformed "current" list
        
"""

current = ['a']*200      # our starting list
combos = [str(current)]     # list of unique coin comibinations as strings

transform(current)

print(combos)

print(len(combos))    