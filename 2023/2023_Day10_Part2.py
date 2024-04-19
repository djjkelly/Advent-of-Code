#!/usr/bin/env python3
#https://adventofcode.com/2023/day/10

with open("2023/2023_Day10_test1_input.txt") as file_object:
    file_content = file_object.readlines()

map_list = []
for line_number,line in enumerate(file_content):
    char_list = []
    for char_number,char in enumerate(line):
        char_list.append(char)
        if char == 'S':
            start_line = line_number
            start_char = char_number
    map_list.append(char_list)
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
    #print(f'Iterating while loop. Current char : \'{current_char}\'')
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
    if (is_starting or next_direction == 'up') and (char_up == '7' or char_up == '|' or char_up == 'F'):
        if char_up == '7':
            next_direction = 'left'
        if char_up == '|':
            next_direction = 'up'
        if char_up == 'F':
            next_direction = 'right'
        map_list[line_number][char_number] = '0'
        next_char = char_up
        line_number -= 1
    elif (is_starting or next_direction == 'left') and (char_left == 'L' or char_left == '-' or char_left == 'F'):
        if char_left == 'L':
            next_direction = 'up'
        if char_left == '-':
            next_direction = 'left'
        if char_left == 'F':
            next_direction = 'down'
        map_list[line_number][char_number] = '0'
        next_char = char_left
        char_number -= 1
    elif (is_starting or next_direction == 'down') and (char_down == 'J' or char_down == '|' or char_down == 'L'):
        if char_down == 'J':
            next_direction = 'left'
        if char_down == '|':
            next_direction = 'down'
        if char_down == 'L':
            next_direction = 'right'
        map_list[line_number][char_number] = '0'
        next_char = char_down
        line_number += 1
    elif (is_starting or next_direction == 'right') and (char_right == 'J' or char_right == '-' or char_right == '7'):
        if char_right == 'J':
            next_direction = 'up'
        if char_right == '-':
            next_direction = 'right'
        if char_right == '7':
            next_direction = 'down'
        map_list[line_number][char_number] = '0'
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
map_list[line_number][char_number] = '0'
#print('Total distance from start:',distance_from_start)
if distance_from_start % 2 == 0:
    farthest_distance = distance_from_start // 2
else:
    farthest_distance = distance_from_start // 2 + 1
print('Farthest distance from start: ', farthest_distance)

for line in map_list:
    new_line =''
    for character in line:
        new_line += character
    print(new_line.strip())

print(instructions_list)

'''
6951 - correct answer found for part1.

'''
