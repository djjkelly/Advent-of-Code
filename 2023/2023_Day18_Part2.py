#!/usr/bin/env python3
#https://adventofcode.com/2023/day/18

folder = '2023/'
filename = '2023_Day18_input'
extension = '.txt'
full_path = folder + filename + extension

with open(full_path,'r') as file_object:
    file_content = file_object.readlines()
down,right = 0,0 #starting position
digger_nodes = [(0,0)]
digger_map = []

perimeter_count = 0 # perimeter count should be the same as the total lengths of all lines

# generate a list of coordinates which define the path of the digger:
for line in file_content:
    line = line.strip()
    #print('line',line)
    hexadecimal = line.split()[2]
    #print('hexadecimal[2:7]:',hexadecimal[2:7])
    number_of_moves = int(hexadecimal[2:7],16)
    perimeter_count += number_of_moves
    #print('number_of_moves',number_of_moves)
    instruction = hexadecimal[-2]
    if instruction == '0':
        right = right + number_of_moves
    elif instruction == '1':
        down = down + number_of_moves
    elif instruction == '2':
        right = right - number_of_moves
    elif instruction == '3':
        down = down - number_of_moves
    digger_nodes.append((down,right))

# use shoelace formula to get area of polygon based on x,y coordinates.
polygon_area = 0
previous_node = (0,0)
for node in digger_nodes:
    top_down_shoelace = previous_node[0] * node[1]
    bottom_up_shoelace = previous_node[1] * node[0]
    area_difference = (bottom_up_shoelace - top_down_shoelace) / 2
    polygon_area += area_difference
    previous_node = node
#print(f'polygon area: {int(polygon_area)}')

full_area = polygon_area + perimeter_count/2 + 1
print('full_area:',int(full_area))

'''
testinput: after excavation, the testinput should give a total lava volume of: 952408144115

Sholace formula actually still works if the centre is inside the polygon so I have not used new_digger_nodes.
The area we're looking for is larger than the area enclosed in the polygon.
On the edges (non-corner perimeter) half the square is outside the polygon but counts as excavated.
On most of the corners, on average half the square is outside and half is inside - the square is counted.
Except on four corners, where three quarters of the square is outside the polygon, but the square counts as inside.

Correct answer obtained: 59574883048274
'''
test_dictionary = {
    '2023_Day18_input':
    {'answer':59574883048274},
}

from testmodule import test_function
test_function(test_dictionary,filename,full_area)