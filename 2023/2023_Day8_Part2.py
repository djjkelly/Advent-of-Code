#!/usr/bin/env python3
#https://adventofcode.com/2023/day/8
import math

folder = '2023/'
filename = '2023_Day8_input'
extension = '.txt'
full_path = folder + filename + extension

with open(full_path) as file_object:
    file_content = file_object.readlines()

instructions = ''
network_map = {}
final_count = 1
start_locations = []
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

def look_up_next_element(location,instruction):
    next_element = network_map[location][instruction]
    return next_element

count_list = []
locations = start_locations
for location_number in range(len(locations)):
    answer_found = False
    count = 0
    location = locations[location_number]
    while answer_found is False:
        for instruction in instructions:
            location = look_up_next_element(location,instruction)
            count += 1
            if location[2] == 'Z':
                answer_found = True
                break
    print('Answer found! location ',locations[location_number],'number of moves: ',count)
    count_list.append(count)
print(count_list)

final_count = math.lcm(*tuple(count_list))

print('Final count: ',final_count)
'''
65387731292816696112780371 - wrong answer, too high. There must be a lower multiple of all these numbers.
23977527174353 = correct answer

'''
test_dictionary = {
    '2023_Day8_input':
    {'answer':23977527174353},
}

from testmodule import test_function
test_function(test_dictionary,filename,final_count)