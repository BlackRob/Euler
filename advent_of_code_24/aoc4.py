safe_reports = 0
input_lists = []
# one mistake - element removed lists
second_chances = []

with open('aoc3_input', 'r') as file:
    # Read each line in the file
    for line in file:
        new_line = line.split()
        for i in range(0,len(new_line)):
            # Converts each element to an integer
            new_line[i] = int(new_line[i])
        input_lists.append(new_line)

def check_list(a_list):
    # we assume each list is safe until we find a mistake
    is_safe = True
    # check if it's ascending
    ascending = False
    if a_list[1] > a_list[0]:
        ascending = True
    # if it's false it's descending or equal
    # if equal, that's a mistake, so remove it
    if a_list[1] == a_list[0]:
        is_safe = False
    for i in range(0,len(a_list) - 1):
        if ascending:
            if a_list[i+1] - a_list[i] > 3 or a_list[i+1] - a_list[i] < 1:
                is_safe = False
        else:   # descending
            if a_list[i] - a_list[i+1] > 3 or a_list[i] - a_list[i+1] < 1:
                is_safe = False
    return is_safe

for a_list in input_lists: 
    # check if it's ascending
    ascending: bool = False
    if a_list[1] > a_list[0]:
        ascending = True
    # if it's false it's descending or equal
    # if equal, that's a mistake, so remove it
    if a_list[1] == a_list[0]:
        second_chances.append(a_list[:])
        continue

    small_steps: bool = True
    for i in range(0,len(a_list) - 1):
        if ascending:
            if a_list[i+1] - a_list[i] > 3 or a_list[i+1] - a_list[i] < 1:
                small_steps = False
                second_chances.append(a_list[:])
                break
        else:   # descending
            if a_list[i] - a_list[i+1] > 3 or a_list[i] - a_list[i+1] < 1:
                small_steps = False
                second_chances.append(a_list[:])
                break
    #print(a_list,mistakes,small_steps)
    if small_steps:
        safe_reports += 1

print("Input lists:", len(input_lists)," Second chances:", len(second_chances))
print("Input lists 0:", input_lists[0]," Second chances 0:", second_chances[0])
print("Input lists 1:", input_lists[1]," Second chances 1:", second_chances[1])
print("Input lists 2:", input_lists[2]," Second chances 2:", second_chances[2])
print("Input lists 3:", input_lists[3]," Second chances 3:", second_chances[3])
print("Input lists 4:", input_lists[4]," Second chances 4:", second_chances[4])
print("Input lists 5:", input_lists[5]," Second chances 5:", second_chances[5])
print("Input lists 6:", input_lists[6]," Second chances 6:", second_chances[6])
print("Input lists 7:", input_lists[7]," Second chances 7:", second_chances[7])
print("Input lists 8:", input_lists[8]," Second chances 8:", second_chances[8])
print("Input lists 9:", input_lists[9]," Second chances 9:", second_chances[9])
print("Input lists 10:", input_lists[10]," Second chances 10:", second_chances[10])
print("Input lists 11:", input_lists[11]," Second chances 11:", second_chances[11])
print("Input lists 12:", input_lists[12]," Second chances 12:", second_chances[12])
print("Input lists 13:", input_lists[13]," Second chances 13:", second_chances[13])
print("Input lists 14:", input_lists[14]," Second chances 14:", second_chances[14])
print("Input lists 15:", input_lists[15]," Second chances 15:", second_chances[15])
print("First pass safe reports: ",safe_reports)

for a_list in second_chances: 
    for i in range(0,len(a_list)):
        new_line = a_list[:]
        del new_line[i]
        good = check_list(new_line)
        if good:
            safe_reports += 1
            break


print("Second pass safe reports: ",safe_reports)

                
