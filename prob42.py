# generate list of triangle numbers (first 1000)
trinum = []

for i in range(1,1001):
    trinum.append(int(i*(i+1)/2))

maxTrinum = max(trinum)

# get our list of words, turn it into a list
f = open('p042_words.txt','r')

wordlist = f.read().replace('"','').split(',')

f.close()

# loop through the list of words, make a sum from
# each words letters, then check if each sum is in
# the list of triangle words; if so, count it
numTriangleWords = 0

for i in range(len(wordlist)):
    wordSum = 0
    for j in range(len(wordlist[i])):
        wordSum += (ord(wordlist[i][j])-64)
    if wordSum in trinum:
        numTriangleWords += 1

print(numTriangleWords)

