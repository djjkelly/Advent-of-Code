#!/usr/bin/env python3
#https://adventofcode.com/2023/day/8

with open("2023/2023_Day8_testinput.txt") as file_object:
    file_content = file_object.readlines()

instructions = ''
network_map = {}
final_count = 0
start_locations = []
target_locations = 'ZZZ'
first_line = True
for line in file_content:
    if first_line:
        instructions += line.strip()
    elif line.strip():
        start = line.split(' = ')[0]
        left = line.split('= (')[1].split(', ')[0]
        right = line.split(', ')[1].split(')')[0]
        network_map[start] = {'L':left, 'R':right}
        if start[2] == 'A':
            start_locations.append(start)
    first_line = False
print(f'network_map loaded. Commencing while loop. start_locations: \n{start_locations}')

# TEST - Correct answer should be 6

def advance_all_elements(locations,instruction):
    next_elements = []
    for location in locations:
        next_element = network_map[location][instruction]
        next_elements.append(next_element)
    return next_elements
#print(f'lookup element test: ',look_up_next_element('DHD','L'))

locations = start_locations
all_locations_arrived = False
locations_arrived = []
while_loop_counter = 0
while not all_locations_arrived:
    while_loop_counter +=1
    print(f'Loop {while_loop_counter}. Not all locations have arrived. While loop continuing...')
    for instruction in instructions: # not convinced this for loop in a while loop structure is still valid for this problem.
        final_count += 1
        locations = advance_all_elements(locations,instruction)
        for location in locations:
            if location[2] == 'Z':
                locations_arrived.append(True)
            else:
                locations_arrived.append(False)
        if all(locations_arrived):
            all_locations_arrived = True
            break

print(final_count)

'''

'''