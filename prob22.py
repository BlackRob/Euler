# get the source data from a file and make it useful
file = open("names.txt","r")
data = file.readlines()
file.close()

names = [x.strip() for x in data[0].split(',')]

items = len(names)
names.sort()

for i in range(items):
    names[i] = names[i][1:-1]


#print(names[937])
#print(names[-1])
#print(names[0])
#print(names[1])
#print(names[3289])

abval = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, \
    'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, \
    'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26
}

name_score = 0
name_score_sum = 0
for i in range(items):
    for c in names[i]:
        name_score += abval[c]
    name_score_sum += (i + 1) * name_score
    name_score = 0


print(name_score_sum)