#!/usr/bin/env python3
#https://adventofcode.com/2023/day/18

with open("2023/2023_Day18_input.txt",'r') as file_object:
    file_content = file_object.readlines()
down,right = 0,0 #starting position
digger_nodes = []
digger_map = []

# generate a list of coordinates which define the path of the digger:
for line in file_content:
    line = line.strip()
    direction = line.split()[0]
    number_of_moves = int(line.split()[1])
    print(f'direction: {direction}. number_of_moves: {number_of_moves}')
    if direction == 'R':
        right = right + number_of_moves
    elif direction == 'D':
        down = down + number_of_moves
    elif direction == 'L':
        right = right - number_of_moves
    elif direction == 'U':
        down = down - number_of_moves
    digger_nodes.append((down,right))
    print(digger_nodes)

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
            #print('m =',m)
            digger_map[down][right + m] = '#'
    elif move_right == 0:
        #print('Moving down or up: move_down:',move_down)
        for m in range(1,abs(move_down)+1):
            if move_down < 0:
                m = -m
            #print('down:',down,'m =',m)
            digger_map[down + m][right] = '#'
    down,right = new_down,new_right
perimeter_count = 0
for line in digger_map:
    perimeter_count += line.count('#')
    #print(line)
print('perimeter count:', perimeter_count)

digger_map.insert(0,['-']*len(digger_map[0]))
digger_map.append(['-']*len(digger_map[0]))
for line_number,line in enumerate(digger_map):
    line.insert(0,'-')
    line.append('-')
    digger_map[line_number] = line

for line in digger_map:
    '''print(line)'''

def search_and_replace(line_number, char_number ,list_of_lists):
    new_coordinates_to_check = []
    if line_number > 0: # searching up
        if list_of_lists[line_number-1][char_number] == '-':
            list_of_lists[line_number-1][char_number] = '0'
            new_coordinates_to_check.append([line_number - 1,char_number])
    if char_number > 0: # searching left
        if list_of_lists[line_number][char_number-1] == '-':
            list_of_lists[line_number][char_number-1] = '0'
            new_coordinates_to_check.append([line_number,char_number - 1])
    if line_number < len(list_of_lists) -1: # searching down
        if list_of_lists[line_number+1][char_number] == '-':
            list_of_lists[line_number+1][char_number] = '0'
            new_coordinates_to_check.append([line_number + 1,char_number])
    if char_number < len(list_of_lists[0]) -1: # searching right
        if list_of_lists[line_number][char_number+1] == '-':
            list_of_lists[line_number][char_number+1] = '0'
            new_coordinates_to_check.append([line_number,char_number+1])
    return new_coordinates_to_check

flood_coordinates = [[0,0]]
flood_coordinates_found = []
while len(flood_coordinates) > 0:
    for coordinate_pair in flood_coordinates:
        line_number = coordinate_pair[0]
        char_number = coordinate_pair[1]
        flood_coordinates.remove(coordinate_pair)
        new_coordinates_to_check = search_and_replace(line_number,char_number,digger_map) # needs to be changed if list is changed
        for coordinate_pair in new_coordinates_to_check:
            if coordinate_pair not in flood_coordinates_found:
                flood_coordinates.append(coordinate_pair)
            coordinate_pair.append(flood_coordinates_found)

total_count = perimeter_count
for line in digger_map:
    line_count = line.count('-')
    total_count += line_count
print(total_count)

'''
there should be 38 cubic metres of lava on the perimeter.
after excavation, the testinput should give a total lava volume of: 62
testinput correct.
input correct too!

'''