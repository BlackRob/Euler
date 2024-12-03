import re
pattern = re.compile(r'mul\([0-9]+,[0-9]+\)')

all_multiplications = 0
input_lines = []

with open('aoc5_input', 'r') as file:
    # Read each line in the file
    for line in file:
        input_lines.append(line)

def extract_ms(mul_string):
    # print(mul_string)
    first_par_index = 4
    comma_index = mul_string.index(",")
    second_par_index = mul_string.index(")")
    m1digs = comma_index - first_par_index
    m2digs = second_par_index - comma_index
    return [int(mul_string[first_par_index:comma_index]),int(mul_string[comma_index+1:second_par_index])]

for line in input_lines:
    mul_strings =  (re.findall(pattern, line))
    for mul in mul_strings:
        multiplicands = extract_ms(mul)
        product = multiplicands[0]*multiplicands[1]
        all_multiplications += product
        print(mul, "=>", multiplicands[0], "*", multiplicands[1], "=", product)

print(all_multiplications)