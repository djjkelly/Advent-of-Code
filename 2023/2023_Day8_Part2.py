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
# print(f'lookup element test: ',advance_all_elements(['11A','22A'],'L')) # should print ['11B', '22B'] for testinput.

def initialise_findings_table(start_locations):
    output = []
    for index in range(len(start_locations)):
        output.append([])
    return output
findings = initialise_findings_table(start_locations)
print(findings)

locations = start_locations
all_locations_arrived = False
i = 0
while not all_locations_arrived:
    locations_arrived = []
    final_count += 1
    if final_count % 1000000 == 0:
        print(f'Loop {final_count}. Not all locations have arrived. While loop continuing...')
    instruction = instructions[i]
    #print('Original locations: ',locations ,'Current instruction: ', instruction )
    locations = advance_all_elements(locations,instruction)
    #print('New locations: ', locations)
    for index,location in enumerate(locations):
        if location[2] == 'Z':
            locations_arrived.append(True)
            findings[index].append(final_count)
            print('Z found!, index: ',final_count)
        else:
            locations_arrived.append(False)
    #print('locations_arrived',locations_arrived)
    if all(locations_arrived):
        all_locations_arrived = True
        #print('all locations arrived!')
        break
    #print('length of locations: ',len(locations))
    i += 1
    if i == len(locations):
        i = 0
print('FINAL COUNT! ',final_count)

'''

'''