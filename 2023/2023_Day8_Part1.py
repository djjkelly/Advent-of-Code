#!/usr/bin/env python3
#https://adventofcode.com/2023/day/7

with open("2023/2023_Day8_input.txt") as file_object:
    file_content = file_object.readlines()

# a rank of 1 means the weakest hand
instructions = []
network_map = {}
first_line = True
for line in file_content:
    if first_line:
        instructions.append(line)
    elif line.strip():
        start = line.split(' = ')[0]
        left = line.split('= (')[1].split(', ')[0]
        right = line.split(', ')[1].split(')')[0]
        network_map[start] = {'L':left, 'R':right}
    first_line = False
print(network_map)
'''

'''