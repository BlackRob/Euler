inputLeft = []
inputRight = []

with open('aoc1_input', 'r') as file:
    # Read each line in the file
    for line in file:
        splitline = line.split()
        inputLeft.append(splitline[0])
        inputRight.append(splitline[1])
        
inputLeft.sort()
inputRight.sort()

for i in range(25):
   print(inputLeft[i],inputRight[i],abs(int(inputRight[i])-int(inputLeft[i])))

totalDistance = 0
for i in range(len(inputLeft)):
    totalDistance += abs(int(inputRight[i])-int(inputLeft[i]))

print(totalDistance)

