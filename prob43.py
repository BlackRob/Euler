# assumes it's given an int
def intLength(x):
    if x < 10:
        return 1
    elif x < 100:
        return 2
    elif x < 1000:
        return 3
    elif x < 10000:
        return 4
    elif x < 100000:
        return 5
    elif x < 1000000:
        return 6
    elif x < 10000000:
        return 7
    elif x < 100000000:
        return 8
    elif x < 1000000000:
        return 9
    elif x < 10000000000:
        return 10
    else:
        return -1

def digNoRepeat(x):
    """ x is an integer, which gets converted to a list of its digits,
        then the list is checked to see if it repeats any of the digits """
    y = []
    x2 = x
    xRef = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
    for i in range(intLength(x)):
        y.append(int(x2 % 10))
        x2 = x2 / 10
    for j in range(len(y)):
        if y[j] in xRef:
            return False
        else:
            xRef[j] = y[j]
    return True

def potentialPandigital(x):
    """ x is a string, 10 characters long; convert it to a list of its chars,
        then check if any of them repeat """
    xRef = ['.','.','.','.','.','.','.','.','.','.']
    for i in range(len(x)):
        if x[i] in xRef:
            return False
        else:  
            xRef[i] = x[i]
    return str.join(xRef)
        

# we're going to fill this in and weed it out
answerCandidates17s = []

# first, all the 3 digit numbers divisible by 17
## that don't repeat digits
numdiv17 = []
i = 0
x = 0
while x < 1000:
    x += 17
    if digNoRepeat(x):
        numdiv17.append(x) 

# next convert all candidates into answerCandidates (strings)
for i in range(len(numdiv17)):
    x = str(numdiv17[i])
    if len(x) < 3:
        x = '0' + x
    frame = ['.','.','.','.','.','.','.','.','.','.']
    frame[7] = x[0]
    frame[8] = x[1]
    frame[9] = x[2]
    answerCandidates17s.append(frame)
print(answerCandidates17s)

# next, all the 3 digit numbers divisible by 13
## that don't repeat digits
numdiv13 = []
i = 0
x = 0
while x < 1000:
    x += 13
    if digNoRepeat(x):
        numdiv13.append(x) 
print(numdiv13)

# combine 17s and 13s; all the ones that match the criterion
# (still pandigital)
# print(digNoRepeat(1234566))