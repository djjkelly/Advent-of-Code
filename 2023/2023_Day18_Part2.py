#!/usr/bin/env python3
#https://adventofcode.com/2023/day/18

with open("2023/2023_Day18_input.txt",'r') as file_object:
    file_content = file_object.readlines()
down,right = 0,0 #starting position
digger_nodes = [(0,0)]
digger_map = []

# generate a list of coordinates which define the path of the digger:
for line in file_content:
    line = line.strip()
    direction = line.split()[0]
    number_of_moves = int(line.split()[1])
    #print(f'direction: {direction}. number_of_moves: {number_of_moves}')
    if direction == 'R':
        right = right + number_of_moves
    elif direction == 'D':
        down = down + number_of_moves
    elif direction == 'L':
        right = right - number_of_moves
    elif direction == 'U':
        down = down - number_of_moves
    digger_nodes.append((down,right))

# find length of the digger map in downward and right directions:
right_max = 0
down_max = 0
right_min = 0
down_min = 0
for node in digger_nodes:
    if node[0] > down_max:
        down_max = node[0]
    if node[0] < down_min:
        down_min = node[0]
    if node[1] > right_max:
        right_max = node[1]
    if node[1] < right_min:
        right_min = node[1]
print('down_max',down_max,'right_max',right_max,'down_min',down_min,'right_min',right_min)
down_length = down_max - down_min
right_length = right_max - right_min
print('down_length:',down_length,'right_length:', right_length)

# set a digger map of the right size:
for down in range(down_length+1):
    digger_map.append([])
    for right in range(right_length+1):
        digger_map[down].append('-')
    #print(digger_map[down])

# excavate lines between nodes:
down,right = 0-down_min,0-right_min
for node in digger_nodes:
    new_down,new_right = node[0] - down_min, node[1] - right_min
    move_down,move_right = new_down - down, new_right - right
    #print('node:',node, 'move_down:' ,move_down,'move_right',move_right)
    if move_down == 0:
        #print('Moving right or left: move_right:',move_right)
        for m in range(1,abs(move_right) + 1):
            if move_right < 0:
                m = -m
            digger_map[down][right + m] = '#'
    elif move_right == 0:
        #print('Moving down or up: move_down:',move_down)
        for m in range(1,abs(move_down)+1):
            if move_down < 0:
                m = -m
            digger_map[down + m][right] = '#'
    down,right = new_down,new_right
perimeter_count = 0
for line in digger_map:
    perimeter_count += line.count('#')
print('perimeter count:', perimeter_count)

digger_map.insert(0,['-']*len(digger_map[0]))
digger_map.append(['-']*len(digger_map[0]))
for line_number,line in enumerate(digger_map):
    line.insert(0,'-')
    line.append('-')
    digger_map[line_number] = line

new_digger_nodes = []
for node in digger_nodes:
    if down_min < 0:
        down = node[0] - down_min + 1
    else:
        down = node[0] + 1
    if right_min < 0:
        right = node[1] - right_min + 1
    else:
        right = node[1] + 1
    new_digger_nodes.append((down,right))
    print('node:',node, 'down:',down,'right:',right)

# use shoelace formula to get area of polygon based on x,y coordinates.
area = 0
previous_node = (275,42)
for node in new_digger_nodes:
    top_down_shoelace = previous_node[0] * node[1]
    bottom_up_shoelace = previous_node[1] * node[0]
    area_difference = (top_down_shoelace - bottom_up_shoelace) / 2
    area += area_difference
    previous_node = node
print(f'area difference: {area_difference}')

'''
testinput: after excavation, the testinput should give a total lava volume of: 952408144115

'''