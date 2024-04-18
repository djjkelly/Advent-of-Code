#!/usr/bin/env python3
#https://adventofcode.com/2023/day/10

with open("2023/2023_Day10_input.txt") as file_object:
    file_content = file_object.readlines()

test1_content = ['.....','.S-7.','.|.|.','.L-J.','.....']
test2_content = ['7-F7-','.FJ|7','SJLL7','|F--J','LJ.LJ']
file_content = test1_content # TEST INPUT !

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
#print(map_list)

print('Commencing analysis. Start point at line index:',start_line,', character index:',start_char)
distance_from_start = 0
char_number = start_char
line_number = start_line
is_starting = True

while map_list[line_number][char_number] != 'S' or is_starting:
    is_starting = False
    current_char = map_list[line_number][char_number]
    print(f'Iterating while loop. Current char : \'{current_char}\'')
    if line_number > 0: # evaluate up
        next_char = map_list[line_number - 1][char_number]
        if next_char == '7' or next_char == '|' or next_char == 'F':
            print('Connected to loop above! next_char = ',next_char)

    if char_number > 0: # evaluate left
        next_char = map_list[line_number][char_number - 1]
        if next_char == 'L' or next_char == '-' or next_char == 'F':
            print('Connected to loop left! next_char = ',next_char)

    if line_number < max_line_number: # evaluate down
        next_char = map_list[line_number + 1][char_number]
        if next_char == 'J' or next_char == '|' or next_char == 'L':
            print('Connected to loop down! next_char = ',next_char)

    if char_number < max_char_number: # evaluate right
        next_char = map_list[line_number][char_number + 1]
        if next_char == 'J' or next_char == '-' or next_char == '7':
            print('Connected to loop right! next_char = ',next_char)
    
print(distance_from_start)

'''
The task is to find the farthest away point on the loop.
There is only one, large loop, meaning only two possible directions of travel.
I see no reason why the loop shouldn't be navigated in a single direction.
The distance_from_start should be half the distance around the whole loop.
The pipes cannot connect diagonally, they can only connect up,down,left,right.
I need to make sure the loop doesn't start counting in the direction it came - I could achieve this by deleting pipes from the map_list as I travel through (replace with '.').
'''