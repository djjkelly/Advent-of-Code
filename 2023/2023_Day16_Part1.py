#!/usr/bin/env python3
#https://adventofcode.com/2023/day/16

with open("2023/2023_Day16_testinput.txt",'r') as file_object:
    file_content = file_object.readlines()
input_list=[]
energisation_map = []
for line in file_content:
    line = line.strip()
    new_line = []
    blank_line = []
    for char in line:
        new_line.append(char) # this puts \\ instead of \
        blank_line.append('')
    print(new_line)
    input_list.append(new_line)
    energisation_map.append(blank_line)

'''
. means transparent

/ turns right to up, left to down, down to left, up to right
(left and down swap, up and right swap)

\ turns right to down, left to up, down to right, up to left - in other words left and up sw
(left and up swap, down and right swap)

splitter - or | means nothing when hit by a beam end-on.
when hit side on, the beam is split into both perpendicular directions.

LIGHT BEAM enters from left, in top-left corner.
'''


def move_to_next(line_no,char_no,direction):
    new_line_no,new_char_no = line_no,char_no
    if direction == 'right':
        new_char_no = char_no + 1
    elif direction == 'down':
        new_line_no = line_no + 1
    elif direction == 'left':
        new_char_no = char_no - 1
    elif direction == 'up':
        new_line_no = line_no - 1
    return(new_line_no,new_char_no)

def explore_branch(line_no,char_no,direction):
    branch_continues = True
    while branch_continues:
        energisation_map[line_no][char_no] = '#'
        line_no,char_no = move_to_next(line_no,char_no,direction) # reassigning line_no and char_no to new values
        if line_no < 0 or char_no < 0 or line_no == len(input_list) or char_no == len(input_list):
            branch_continues = False
            print(f'end of branch at line: {line_no} char: {char_no}')
            break
        if input_list[line_no][char_no] == '.':
            continue
        # setting next direction...
        if input_list[line_no][char_no] == '/':
            if direction == 'right':
                direction = 'up'
            elif direction == 'down':
                direction = 'left'
            elif direction == 'left':
                direction = 'down'
            elif direction == 'up':
                direction = 'right'
        elif input_list[line_no][char_no] == '\\':
            if direction == 'right':
                direction = 'down'
            elif direction == 'down':
                direction = 'right'
            elif direction == 'left':
                direction = 'up'
            elif direction == 'up':
                direction = 'left'
        elif input_list[line_no][char_no] == '-':
            if direction == 'right' or direction == 'left':
                continue
            if direction == 'down' or direction == 'up':
                direction = 'left'
                list_of_branches_to_explore.append({'line_no':line_no,'char_no':char_no,'direction':'right'})
        elif input_list[line_no][char_no] == '|':
            if direction == 'down' or direction == 'up':
                continue
            if direction == 'right' or direction == 'left':
                direction = 'up'
                list_of_branches_to_explore.append({'line_no':line_no,'char_no':char_no,'direction':'down'})


list_of_branches_to_explore = [{'line_no':0,'char_no':0,'direction':'right'}] # initial direction 'right' upon beam entering array
branch_continues = True
while list_of_branches_to_explore != []:
    line_no = list_of_branches_to_explore[0]['line_no']
    char_no = list_of_branches_to_explore[0]['char_no']
    direction = list_of_branches_to_explore[0]['direction']
    list_of_branches_to_explore.pop(0)
    explore_branch(line_no,char_no,direction)
energised_tiles_no = 0

for line in energisation_map:
    line_count = line.count('#')
    energised_tiles_no += line_count

'''
testinput should give a number of energised tiles of: 46

'''