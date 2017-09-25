distinct_powers = []
x = 0

for a in range(2,101):
    for b in range(2,101):
        x = a**b
        if x in distinct_powers:
            pass
        else:
            distinct_powers.append(x)

print(len(distinct_powers))