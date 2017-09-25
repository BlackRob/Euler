def digitify(n):
    l = []
    while n > 0:
        l.append(n%10)
        n = n // 10
    return l

digits =[]
for a in range(0,10):
    digits.append( a**5 )

sum = 0
superSum = 0
workingNum = []

print(digits)

for i in range(2,360000):
    workingNum = digitify(i)
    #print(i,workingNum)
    for j in range(len(workingNum)):
        sum += digits[workingNum[j]]
    if sum == i:
        print(i)
        superSum += sum
    sum = 0

print(superSum)