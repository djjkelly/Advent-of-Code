#!/usr/bin/env python3
#https://adventofcode.com/2023/day/17

with open("2023/2023_Day17_testinput.txt",'r') as file_object:
    file_content = file_object.readlines()
input_list = []
for line in file_content:
    line = line.strip()
    input_list.append(line)
    print(line)
line_length = len(line)
column_length = len(input_list)

'''
each character represents a block with a per-block heat loss.
current node can move in 4 different directions (no diagonals).
max blocks in one line = 3
'''
minimum_heat_loss_estimates = [[float('inf')] * line_length for _ in range(column_length)]
minimum_heat_loss_estimates[0][0] = 0
for line in minimum_heat_loss_estimates:
    print(line)

current_node = (0,0)
while current_node != (line_length,column_length):
    previous_direction_vectors = [[0,0][0,0][0,0]]
    # update estimates
        # check all 4 directions (if the direction exists in the map)
        # assign each of the 4 nodes (or 3 nodes if previous_direction_vectors match) with a new estimate if lower than current estimate
            # new estimate will be the estimate at the current node plus the heat loss at the new node

    # move current node to lowest adjacent unexplored node (unexplored means not 0 or infinity)

'''
testinput should give a heat loss of: 102

'''