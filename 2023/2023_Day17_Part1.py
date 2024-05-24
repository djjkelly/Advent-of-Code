#!/usr/bin/env python3
#https://adventofcode.com/2023/day/17

import heapq

with open("2023/2023_Day17_testinput.txt",'r') as file_object:
    file_content = file_object.readlines()
input_list = []
for line in file_content:
    line = line.strip()
    input_list.append(line)
horizontal_length = len(line)
vertical_length = len(input_list)

'''
each character represents a block with a per-block heat loss (1-9).
max blocks in one direction = 3
'''
minimum_heat_loss_estimates = [[float('inf')] * horizontal_length for _ in range(vertical_length)]
previous_directions = [[[None,None,None] for _ in range(horizontal_length)] for _ in range(vertical_length)]
explored_map = [[False] * horizontal_length for _ in range(vertical_length)]
minimum_heat_loss_estimates[0][0] = 0
directions = {
    'down':(1,0),
    'right':(0,1),
    'up':(-1,0),
    'left':(0,-1)
}

def is_in_bounds(v,h):
    return 0 <= v < vertical_length and 0 <= h < horizontal_length

def is_direction_permitted(direction, directions_to_check):
    print('checking direction' ,direction, 'against directions_to_check: ',directions_to_check)
    for d in directions_to_check:
        if d != direction:
            print('is_direction_permitted function returns True!')
            return True
    print('is_direction_permitted function returns False!')
    return False

queue = [(0,0,0)]
while queue:
    current_heat_loss,v,h = heapq.heappop(queue)
    explored_map[v][h] = True
    # update estimates
    print(f'\nCurrent_heat_loss {current_heat_loss} at location vert {v} and horiz {h}')
    # check all 4 directions (if the direction exists in the map)
    for direction,(vert_move,horiz_move) in directions.items():
        new_v = v + vert_move
        new_h = h + horiz_move
        print(f'direction being considered: {direction}. New coordinates: vert {new_v} horiz {new_h}')
        if is_in_bounds(new_v,new_h) and not explored_map[new_v][new_h]:
            new_estimate = int(input_list[new_v][new_h]) + current_heat_loss
            print(f'new estimate to consider for vert {new_v} horiz {new_h} with direction {direction}: new estimate = {new_estimate}')
            directions_to_check = previous_directions[v][h]
            if is_direction_permitted(direction, directions_to_check):
                if new_estimate < minimum_heat_loss_estimates[new_v][new_h]:
                    minimum_heat_loss_estimates[new_v][new_h] = new_estimate
                    print(f'updating previous directions at new_v,new_h!: {previous_directions[v][h][1:]},{direction}')
                    previous_directions[new_v][new_h] = previous_directions[v][h][1:] + [direction]
                    heapq.heappush(queue, (new_estimate, new_v, new_h))
                    print(f"Updated directions at ({new_v}, {new_h}): {previous_directions[new_v][new_h]}")
print(minimum_heat_loss_estimates[-1][-1])

# follow path back to start point
best_path = [list(row) for row in input_list]
v, h = vertical_length - 1, horizontal_length - 1
symbols = {
    'down': 'v',
    'right': '>',
    'up': '^',
    'left': '<' }
while v > 0 or h > 0:
    direction = previous_directions[v][h][-1]
    best_path[v][h] = symbols[direction]
    dv, dh = directions[direction]
    v, h = v - dv, h - dh
best_path[0][0] = 'S'
best_path[vertical_length - 1][horizontal_length - 1] = 'E'
for line in best_path:
    print(''.join(line))

'''
testinput should give a heat loss of: 102
'''
