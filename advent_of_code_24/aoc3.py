safe_reports = 0
input_lists = []

with open('aoc3_input', 'r') as file:
    # Read each line in the file
    for line in file:
        new_line = line.split()
        for i in range(0,len(new_line)):
            # Converts each element to an integer
            new_line[i] = int(new_line[i])
        input_lists.append(new_line)
        
for a_list in input_lists: 
    # check if it's ascending
    ascending: bool = False
    if a_list[1] > a_list[0]:
        ascending = True
    # if it's false it's descending, if equal skip to next
    if a_list[1] == a_list[0]:
        continue

    # stable_scending: bool = True
    small_steps: bool = True
    for i in range(0,len(a_list) - 1):
        if ascending:
            # if a_list[i] < a_list[i+1]:
            #     stable_scending = False
            #     continue
            if a_list[i+1] - a_list[i] > 3 or a_list[i+1] - a_list[i] < 1:
                small_steps = False
                continue
        else:   # descending
            # if a_list[i] > a_list[i+1]:
            #     stable_scending = False
            #     continue
            if a_list[i] - a_list[i+1] > 3 or a_list[i] - a_list[i+1] < 1:
                small_steps = False
                continue
    if small_steps: # and stable_scending: 
        safe_reports += 1

print(safe_reports)

                
