#!/usr/bin/env python3
#https://adventofcode.com/2023/day/8

with open("2023/2023_Day8_input.txt") as file_object:
    file_content = file_object.readlines()

# a rank of 1 means the weakest hand
instructions = ''
network_map = {}
final_count = 0
first_location = ''
target_location = 'ZZZ'
first_line = True
for line in file_content:
    if first_line:
        instructions += line.strip()
    elif line.strip():
        start = line.split(' = ')[0]
        left = line.split('= (')[1].split(', ')[0]
        right = line.split(', ')[1].split(')')[0]
        network_map[start] = {'L':left, 'R':right}
        if first_location == '':
            first_location = start
    first_line = False
#print(network_map)

''' # TEST SECTION
instructions = 'LLR' # TEST INPUT FROM EXAMPLE
network_map = {'AAA':{'L':'BBB','R':'BBB'},'BBB':{'L':'AAA','R':'ZZZ'},'ZZZ':{'L':'ZZZ','R':'ZZZ'}} # TEST INPUT FROM EXAMPLE
first_location = 'AAA' # TEST INPUT FROM EXAMPLE
# Correct answer obtained - 6'''

def look_up_next_element(location,instruction):
    next_element = network_map[location][instruction]
    return next_element
#print(f'lookup element test: ',look_up_next_element('DHD','L'))

location = first_location
while location != target_location:
    for instruction in instructions:
        location = look_up_next_element(location,instruction)
        final_count += 1
print(final_count)

'''

'''