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
previous_directions = [[[] for _ in range(horizontal_length)] for _ in range(vertical_length)]
previous_directions[0][0] = None
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

def direction_permitted(new_vert, new_horiz, direction, previous_directions, directions):
    vert_move, horiz_move = directions[direction]
    consecutive_count = 0
    for i in range(1, 4):
        check_vert = new_vert - vert_move * i
        check_horiz = new_horiz - horiz_move * i
        if not is_in_bounds(check_vert,check_horiz):
            return True
        prev_direction = previous_directions[check_vert][check_horiz]
        if prev_direction is None or prev_direction != direction:
            return True
        consecutive_count += 1
        if consecutive_count == 3:
            print(f'                        Returning FALSE! Direction not permitted {direction} ')
            return False
    return True

queue = [(0,0,0)]
while queue:
    current_heat_loss,vert_coord,horiz_coord = heapq.heappop(queue)
    explored_map[vert_coord][horiz_coord] = True
    # update estimates
    print(f'\nCurrent_heat_loss {current_heat_loss} at location vert {vert_coord} and horiz {horiz_coord}')
    # check all 4 directions (if the direction exists in the map)
    for direction,(vert_move,horiz_move) in directions.items():
        new_vert = vert_coord + vert_move
        new_horiz = horiz_coord + horiz_move
        print(f'direction being considered: {direction}. New coordinates: vert {new_vert} horiz {new_horiz}')
        if is_in_bounds(new_vert,new_horiz) and not explored_map[new_vert][new_horiz]:
            new_estimate = int(input_list[new_vert][new_horiz]) + current_heat_loss
            print(f'new estimate to consider for vert {new_vert} horiz {new_horiz} with direction {direction}: new estimate = {new_estimate}')
            if direction_permitted(new_vert,new_horiz,direction,previous_directions,directions):
                print(f'direction permitted!')
                if new_estimate < minimum_heat_loss_estimates[new_vert][new_horiz]:
                    minimum_heat_loss_estimates[new_vert][new_horiz] = new_estimate
                    previous_directions[new_vert][new_horiz] = direction
                    heapq.heappush(queue,(new_estimate,new_vert,new_horiz))
                    print(f"Updated directions at ({new_vert}, {new_horiz}): {previous_directions[new_vert][new_horiz]}")
            else:
                print('three in a row limit aready reached!')
print(minimum_heat_loss_estimates[-1][-1])

# follow path back to start point
best_path = [list(row) for row in input_list]  # Start with the numbers from the input list
v, h = vertical_length - 1, horizontal_length - 1
symbols = {
    'down': 'v',
    'right': '>',
    'up': '^',
    'left': '<' }
while v > 0 or h > 0:
    direction = previous_directions[v][h]
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