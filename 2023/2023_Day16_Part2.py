#!/usr/bin/env python3
#https://adventofcode.com/2023/day/16

folder = '2023/'
filename = '2023_Day16_input'
extension = '.txt'
full_path = folder + filename + extension

with open(full_path,'r') as file_object:
    file_content = file_object.readlines()
input_list=[]
energisation_map = []
for line in file_content:
    line = line.strip()
    new_line = []
    string = ''
    for char in line:
        new_line.append(char) # this puts \\ instead of \
        if char == '\\':
            string += 'b'
        else:
            string += char
    #print(new_line)
    input_list.append(new_line)
    energisation_map.append(string)

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

def explore_branch(line_no,char_no,direction,local_energisation_map):
    branch_continues = True
    while branch_continues:
        if char_no != -1 and line_no != -1 and char_no < len(new_line) and line_no < len(input_list):
            local_energisation_map[line_no] = local_energisation_map[line_no][:char_no] + '#' + local_energisation_map[line_no][char_no+1:]
        direction_checked = {'line_no':line_no,'char_no':char_no,'direction':direction}
        if direction_checked not in directions_checked:
            directions_checked.append(direction_checked)
        else:
            branch_continues = False
            break
        line_no,char_no = move_to_next(line_no,char_no,direction) # reassigning line_no and char_no to new values
        if line_no < 0 or char_no < 0 or line_no == len(input_list) or char_no == len(input_list):
            branch_continues = False
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
                if {'line_no':line_no,'char_no':char_no,'direction':'right'} not in list_of_historic_branches_explored:
                    if {'line_no':line_no,'char_no':char_no,'direction':'right'} not in list_of_branches_to_explore:
                        list_of_branches_to_explore.append({'line_no':line_no,'char_no':char_no,'direction':'right'})
        elif input_list[line_no][char_no] == '|':
            if direction == 'down' or direction == 'up':
                continue
            if direction == 'right' or direction == 'left':
                direction = 'up'
                if {'line_no':line_no,'char_no':char_no,'direction':'down'} not in list_of_historic_branches_explored:
                    if {'line_no':line_no,'char_no':char_no,'direction':'down'} not in list_of_branches_to_explore:
                        list_of_branches_to_explore.append({'line_no':line_no,'char_no':char_no,'direction':'down'})

def calculate_energised_tiles(start_line,start_char,start_direction):
    global list_of_branches_to_explore
    list_of_branches_to_explore = [{'line_no':start_line,'char_no':start_char,'direction':start_direction}]
    global list_of_historic_branches_explored
    list_of_historic_branches_explored = []
    global directions_checked
    global maximum_energised_tiles
    directions_checked = []
    local_energisation_map = energisation_map.copy()
    while list_of_branches_to_explore != []:
        line_no = list_of_branches_to_explore[0]['line_no']
        char_no = list_of_branches_to_explore[0]['char_no']
        direction = list_of_branches_to_explore[0]['direction']
        historic_branch = list_of_branches_to_explore.pop(0)
        if historic_branch not in list_of_historic_branches_explored:
            list_of_historic_branches_explored.append(historic_branch)
        explore_branch(line_no,char_no,direction,local_energisation_map)
    energised_tiles_no = 0
    for line in local_energisation_map:
        line_count = line.count('#')
        energised_tiles_no += line_count
    print('energised_tiles_no',energised_tiles_no)
    if energised_tiles_no > maximum_energised_tiles:
        maximum_energised_tiles = energised_tiles_no

row_length = len(input_list[0])
column_length = len(input_list)

maximum_energised_tiles = 0

for line_number in range(column_length): # entering array from left: direction = 'right'
    calculate_energised_tiles(line_number,-1,'right')

for line_number in range(column_length): # entering array from right: direction = 'left'
    calculate_energised_tiles(line_number,row_length,'left')

for char_number in range(len(input_list[0])): # entering array from top: direction = 'down'
    calculate_energised_tiles(-1,char_number,'down')

for char_number in range(len(input_list[0])): # entering array from bottom: direction = 'up'
    calculate_energised_tiles(column_length,char_number,'up')

print('max energised_tiles_no',maximum_energised_tiles)
'''
testinput should give a number of energised tiles of: 51

'''
test_dictionary = {
    '2023_Day16_input':
    {'answer':8225},
}

from testmodule import test_function
test_function(test_dictionary,filename,maximum_energised_tiles)