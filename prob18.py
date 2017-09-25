# input for the problem copied and pasted into separate file
# open file, read the lines into a list, close the file
file = open("prob18input","r")
data = file.readlines()
file.close()

# each member of the list data is a string of intgers
# we need to break each line into a list of the separate entries
m = len(data)
i = 0
work = []
while i < m:
    row = data[i].split()
    work.append(row)
    print(work[i])
    i = i + 1

# starting from the bottom of the pyramid, work up
while m >=2:
    rowNext = work[m - 2]
    rowBottom = work[m -1]
    for item in range(0,m-1):
        rowNext[item] = max(int(rowBottom[item]),int(rowBottom[item+1])) + int(rowNext[item])
    print(rowNext)
    m -= 1
    
