#!/usr/bin/env python3
#https://adventofcode.com/2023/day/17

with open("2023/2023_Day17_testinput.txt",'r') as file_object:
    file_content = file_object.readlines()
input_list = []
for line in file_content:
    line = line.strip()
    input_list.append(line)
    print(line)
horizontal_length = len(line)
vertical_length = len(input_list)

'''
each character represents a block with a per-block heat loss.
current node can move in 4 different directions (no diagonals).
max blocks in one line = 3
'''
minimum_heat_loss_estimates = [[float('inf')] * horizontal_length for _ in range(vertical_length)]
explored_map = [[0] * horizontal_length for _ in range(vertical_length)]
minimum_heat_loss_estimates[0][0] = int(input_list[0][0])
for line in minimum_heat_loss_estimates:
    print(line)

current_node = {'vertical':0,'horizontal':0} # (vertical, horizontal)
while current_node['vertical'] != horizontal_length or current_node['horizontal'] != vertical_length:
    previous_direction_vectors = [[0,0],[0,0],[0,0]]
    next_direction = ''
    vert_coord,horiz_coord = current_node['vertical'],current_node['horizontal']
    explored_map[vert_coord][horiz_coord] = 1
    # update estimates
    current_estimate = minimum_heat_loss_estimates[vert_coord][horiz_coord]
    best_estimate = float('inf')
        # check all 4 directions (if the direction exists in the map)
    if vert_coord < vertical_length:
        down_estimate = int(input_list[vert_coord+1][horiz_coord]) + current_estimate
        if down_estimate < minimum_heat_loss_estimates[vert_coord+1][horiz_coord]:
            minimum_heat_loss_estimates[vert_coord+1][horiz_coord] = down_estimate
        if down_estimate < best_estimate and explored_map[vert_coord+1][horiz_coord] == 0:
            best_estimate = down_estimate
            next_direction = 'down'
    if horiz_coord < horizontal_length:
        right_estimate = int(input_list[vert_coord][horiz_coord+1]) + current_estimate
        if  right_estimate < minimum_heat_loss_estimates[vert_coord][horiz_coord+1]:
            minimum_heat_loss_estimates[vert_coord][horiz_coord+1] = right_estimate
        if right_estimate < best_estimate and explored_map[vert_coord][horiz_coord+1] == 0:
            best_estimate = right_estimate
            next_direction = 'right'
    if vert_coord > 0:
        up_estimate = int(input_list[vert_coord-1][horiz_coord]) + current_estimate
        if down_estimate < minimum_heat_loss_estimates[vert_coord-1][horiz_coord]:
            minimum_heat_loss_estimates[vert_coord-1][horiz_coord] = up_estimate
        if up_estimate < best_estimate and explored_map[vert_coord-1][horiz_coord] == 0:
            best_estimate = up_estimate
            next_direction = 'up'
    if horiz_coord > 0:
        left_estimate = int(input_list[vert_coord][horiz_coord-1]) + current_estimate
        if left_estimate < minimum_heat_loss_estimates[vert_coord][horiz_coord-1]:
            minimum_heat_loss_estimates[vert_coord][horiz_coord-1] = left_estimate
        if left_estimate < best_estimate and explored_map[vert_coord][horiz_coord-1] == 0:
            best_estimate = left_estimate
            next_direction = 'left'
        # assign each of the 4 nodes (or 3 nodes if previous_direction_vectors match) with a new estimate if lower than current estimate
            # new estimate will be the estimate at the current node plus the heat loss at the new node
    if next_direction == 'down':
        print('down')
        current_node['vertical'] += 1
    elif next_direction == 'right':
        print('right')
        current_node['horizontal'] += 1 
    elif next_direction == 'up':
        print('up')
        current_node['vertical'] -= 1
    elif next_direction == 'left':
        print('left')
        current_node['horizontal'] -= 1
    # move current node to lowest adjacent unexplored node (unexplored means not 0 or infinity)
    
'''
testinput should give a heat loss of: 102

'''