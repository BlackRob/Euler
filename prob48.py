sum = 0
i = 1

while i <= 1000:
    sum += i**i 
    # print(i**i,sum)
    i += 1

print(sum%10000000000)
