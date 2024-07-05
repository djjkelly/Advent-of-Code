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

\\ turns right to down, left to up, down to right, up to left - in other words left and up sw
(left and up swap, down and right swap)

splitter - or | means nothing when hit by a beam end-on.
when hit side on, the beam is split into both perpendicular directions.

LIGHT BEAM enters from left, in top-left corner.
'''

energised_tiles = set()
directions = {
        'right': (0, 1), 'down': (1, 0), 'up': (-1, 0), 'left': (0, -1)
    }
mirror_reflections = {
        '/': {'right': 'up', 'up': 'right', 'left': 'down', 'down': 'left'},
        '\\': {'right': 'down', 'down': 'right', 'left': 'up', 'up': 'left'}
    }
splitters = {

}

list_of_branches_to_explore = [(0,0,'right')] # initial direction 'right' upon beam entering array
seen_beams = set()
while list_of_branches_to_explore != []:
    current_beam = list_of_branches_to_explore.pop(0)
    if current_beam not in seen_beams:
        seen_beams.append(current_beam)
    branch_continues = True
    while branch_continues:
        (r,c,direction) = current_beam
        energisation_map[r][c] = '#'
        (dr,dc) = directions[direction]
        nr , nc = r + dr , c + dc
        if nr < 0 or nc < 0 or r == len(input_list) or c == len(input_list):
            branch_continues = False
            print(f'end of branch at line: {r} char: {c}')
            break
        current_tile = input_list[r][c]

energised_tiles_no = 0
for line in energisation_map:
    line_count = line.count('#')
    energised_tiles_no += line_count

print('energised_tiles_no',energised_tiles_no)
'''
testinput should give a number of energised tiles of: 46
Test input calculating correctly.

Correct answer obtained = 8034
'''
test_dictionary = {
    '2023_Day16_input':
    {'answer':8034},
}

from testmodule import test_function
test_function(test_dictionary,filename,energised_tiles_no)