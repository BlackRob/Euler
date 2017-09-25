sum = 1
for n in range(3,1003,2):
    sum += 4*n**2 - 6 * (n-1)
    print(n)

print(sum)