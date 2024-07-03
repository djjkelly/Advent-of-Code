#!/usr/bin/env python3
#https://adventofcode.com/2023/day/10

folder = '2023/'
filename = '2023_Day10_input'
extension = '.txt'
full_path = folder + filename + extension

with open(full_path) as file_object:
    file_content = file_object.readlines()

map_list = []
route_list = []
for line_number,line in enumerate(file_content):
    char_list = []
    blank_row = []
    line = line.strip()
    for char_number,char in enumerate(line):
        char_list.append(char)
        blank_row.append('.')
        if char == 'S':
            start_line = line_number
            start_char = char_number
    map_list.append(char_list)
    route_list.append(blank_row)
    max_line_number = line_number
    max_char_number = char_number

print('Commencing analysis. Start point at line index:',start_line,', character index:',start_char)
distance_from_start = 0
char_number = start_char
line_number = start_line
is_starting = True
next_direction = ''
instructions_list = []

while map_list[line_number][char_number] != 'S' or is_starting:
    current_char = map_list[line_number][char_number]
    map_list[line_number][char_number] = '0'
    route_list[line_number][char_number] = current_char
    distance_from_start += 1
    if line_number > 0: # setting char_above
        char_up = map_list[line_number - 1][char_number]
    else:
        char_up = ''
    if char_number > 0: # setting char_left
        char_left = map_list[line_number][char_number - 1]
    else:
        char_left = ''
    if line_number < max_line_number: # setting char_below
        char_down = map_list[line_number + 1][char_number]
    else:
        char_down = ''
    if char_number < max_char_number: # setting char_right
        char_right = map_list[line_number][char_number + 1]
    else:
        char_right = ''
    if is_starting:
        if char_up == '7' or char_up == '|' or char_up == 'F':
            initial_direction = 'up'
        elif char_left == 'L' or char_left == '-' or char_left == 'F':
            initial_direction = 'left'
        elif char_down == 'J' or char_down == '|' or char_down == 'L':
            initial_direction = 'down'
        elif char_right == 'J' or char_right == '-' or char_right == '7':
            initial_direction = 'down'
        instructions_list.append(initial_direction)
    if (is_starting or next_direction == 'up') and (char_up == '7' or char_up == '|' or char_up == 'F'):
        if char_up == '7':
            next_direction = 'left'
        if char_up == '|':
            next_direction = 'up'
        if char_up == 'F':
            next_direction = 'right'
        next_char = char_up
        line_number -= 1
    elif (is_starting or next_direction == 'left') and (char_left == 'L' or char_left == '-' or char_left == 'F'):
        if char_left == 'L':
            next_direction = 'up'
        if char_left == '-':
            next_direction = 'left'
        if char_left == 'F':
            next_direction = 'down'
        next_char = char_left
        char_number -= 1
    elif (is_starting or next_direction == 'down') and (char_down == 'J' or char_down == '|' or char_down == 'L'):
        if char_down == 'J':
            next_direction = 'left'
        if char_down == '|':
            next_direction = 'down'
        if char_down == 'L':
            next_direction = 'right'
        next_char = char_down
        line_number += 1
    elif (is_starting or next_direction == 'right') and (char_right == 'J' or char_right == '-' or char_right == '7'):
        if char_right == 'J':
            next_direction = 'up'
        if char_right == '-':
            next_direction = 'right'
        if char_right == '7':
            next_direction = 'down'
        next_char = char_right
        char_number += 1
    elif char_up == '0' or char_left == '0' or char_down == '0' or char_right == '0':
        print('Loop closed')
        next_char == '0'
        char_number += 1
        break
    #print('next_char: ',next_char,'. Current distance_from_start :',distance_from_start)
    is_starting = False
    instructions_list.append(next_direction)
print('Total distance from start:',distance_from_start)

route_list.insert(0,['.']*len(route_list[0]))
route_list.append(['.']*len(route_list[0]))
for line_number,line in enumerate(route_list):
    line.insert(0,'.')
    line.append('.')
    new_line =''
    for character in line:
        new_line += character
    print(new_line)
    route_list[line_number] = list(new_line)

expanded_list = []
max_line_number = len(route_list)
max_char_number = len(route_list[0])
for line in route_list:
    new_line = []
    for character in line:
        new_line.append(character)
        new_line.append(' ')
    expanded_list.append(new_line)
    expanded_list.append(([' ']* len(new_line)))

#for row in expanded_list:
    #print(''.join(row))

line_number = (start_line+1) * 2
char_number = (start_char+1) * 2
for i in range(distance_from_start):
    if instructions_list[i] == 'up':
        line_number -= 1
        if expanded_list[line_number][char_number] == ' ':
            expanded_list[line_number][char_number] = 'x'
        line_number -= 1
        if expanded_list[line_number][char_number] == ' ':
            expanded_list[line_number][char_number] = 'x'
    if instructions_list[i] == 'left':
        char_number -= 1
        if expanded_list[line_number][char_number] == ' ':
            expanded_list[line_number][char_number] = 'x'
        char_number -= 1
        if expanded_list[line_number][char_number] == ' ':
            expanded_list[line_number][char_number] = 'x'
    if instructions_list[i] == 'down':
        line_number += 1
        if expanded_list[line_number][char_number] == ' ':
            expanded_list[line_number][char_number] = 'x'
        line_number += 1
        if expanded_list[line_number][char_number] == ' ':
            expanded_list[line_number][char_number] = 'x'
    if instructions_list[i] == 'right':
        char_number += 1
        if expanded_list[line_number][char_number] == ' ':
            expanded_list[line_number][char_number] = 'x'
        char_number += 1
        if expanded_list[line_number][char_number] == ' ':
            expanded_list[line_number][char_number] = 'x'

#for row in expanded_list:
    #print(''.join(row))

def search_and_replace(line_number, char_number ,list_of_lists):
    new_coordinates_to_check = []
    if line_number > 0: # searching up
        if list_of_lists[line_number-1][char_number] == '.' or list_of_lists[line_number-1][char_number] == ' ':
            list_of_lists[line_number-1][char_number] = '0'
            new_coordinates_to_check.append([line_number - 1,char_number])
    if char_number > 0: # searching left
        if list_of_lists[line_number][char_number-1] == '.' or list_of_lists[line_number][char_number-1] == ' ':
            list_of_lists[line_number][char_number-1] = '0'
            new_coordinates_to_check.append([line_number,char_number - 1])
    if line_number < len(list_of_lists) -1: # searching down
        if list_of_lists[line_number+1][char_number] == '.' or list_of_lists[line_number+1][char_number] == ' ':
            list_of_lists[line_number+1][char_number] = '0'
            new_coordinates_to_check.append([line_number + 1,char_number])
    if char_number < len(list_of_lists[0]) -1: # searching right
        if list_of_lists[line_number][char_number+1] == '.' or list_of_lists[line_number][char_number+1] == ' ':
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
        new_coordinates_to_check = search_and_replace(line_number,char_number,expanded_list) # needs to be changed if list is changed
        for coordinate_pair in new_coordinates_to_check:
            if coordinate_pair not in flood_coordinates_found:
                flood_coordinates.append(coordinate_pair)
            coordinate_pair.append(flood_coordinates_found)
    #for line in expanded_list: # needs to be changed if list is changed
        #print(''.join(line))
    #print(flood_coordinates)

total_count = 0
for line in expanded_list:
    line_count = line.count('.')
    total_count += line_count
print(total_count)

'''
My interpretation is that you need to start from the outside, as the edge of the data is the main distinguishing factor differentiating inside vs outside.
If there's a '.' on the first/last row or column, it must be outside the loop.
By adding a row and column before and after the data I can make sure all outside regions are connected.

Correct test1 answer obtained of 4
Correct test2 answer obtained of 8
Correct final answer of 563 obtained.

'''
test_dictionary = {
    '2023_Day10_input':
    {'answer':563},
}

from testmodule import test_function
test_function(test_dictionary,filename,total_count)