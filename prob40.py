marker = 0
ourStringLength = 0
ourString = ""
x = 0
d1 = 1
d10 = 1
d100 = 1
d1000 = 1
d10000 = 1
d100000 = 1
d1000000 = 1

for i in range(marker,10):
    x += 1
    ourString = ourString + str(x)
    ourStringLength += len(str(x))
d1 = ourString[0]
d10 = ourString[9]

for i in range(marker+1,100):
    x += 1
    ourString = ourString + str(x)
    ourStringLength += len(str(x))
d100 = ourString[99]

for i in range(marker+1,1000):
    x += 1
    ourString = ourString + str(x)
    ourStringLength += len(str(x))
d1000 = ourString[999]

for i in range(marker+1,10000):
    x += 1
    ourString = ourString + str(x)
    ourStringLength += len(str(x))
d10000 = ourString[9999]

for i in range(marker+1,100000):
    x += 1
    ourString = ourString + str(x)
    ourStringLength += len(str(x))
d100000 = ourString[99999]

for i in range(marker+1,1000000):
    x += 1
    ourString = ourString + str(x)
    ourStringLength += len(str(x))
d1000000 = ourString[999999]

print(d1,d10,d100,d1000,d10000,d100000,d1000000)
print(int(d1)*
    int(d10)*
    int(d100)*
    int(d1000)*
    int(d10000)*
    int(d100000)*
    int(d1000000))