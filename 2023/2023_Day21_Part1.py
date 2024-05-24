#!/usr/bin/env python3
#https://adventofcode.com/2023/day/21

import copy

with open("2023/2023_Day21_input.txt",'r') as file_object:
    file_content = file_object.readlines()

input_list = []
for line_no,line in enumerate(file_content):
    line = line.strip()
    for char_no,char in enumerate(line):
        if char == 'S':
            start_char = char_no
            start_line = line_no
    input_list.append(line)
vertical_length = line_no
horizontal_length = char_no
print(f'start point. line: {start_line} char: {start_char}')
'''
I think that once a location has been explored, it will alternate between '0' and '.'
This means the entire grid can be considered even or odd.
I think this means the whole grid can be evaluated in a single fill operation.
'''
def is_in_bounds(new_coordinates):
    v,h = new_coordinates
    return 0 <= v < vertical_length and 0 <= h < horizontal_length

directions = {
    'down':(1,0),
    'right':(0,1),
    'up':(-1,0),
    'left':(0,-1)
}
number_of_steps = 64 # change to 64 when using real input!
step_count = 0
squares_to_evaluate = [((start_line,start_char),'even')]
squares_evaluated = [((start_line,start_char),'even')]
for step_count in range(number_of_steps):
    current_squares_to_evaluate = copy.deepcopy(squares_to_evaluate)
    squares_to_evaluate = []
    while current_squares_to_evaluate:
        print('\nNEW STEP! Current squares to evaluate:\n',current_squares_to_evaluate)
        current_square = current_squares_to_evaluate.pop(0)
        current_coordinates = current_square[0]
        current_status = current_square[1]
        for directions_item in directions.items():
            direction,move = directions_item[0],directions_item[1]
            print('direction:', direction, ', move:', move)
            new_coordinates = tuple(x+y for x,y in zip(current_coordinates,move))
            print('current_coordinates:',current_coordinates,' new_coordinates:',new_coordinates)
            if not is_in_bounds(new_coordinates):
                print('out of bounds!')
                continue
            if input_list[new_coordinates[0]][new_coordinates[1]] == '#':
                print('hashtag found in direction',direction,'ignoring this square')
                continue
            if current_status == 'odd':
                new_status = 'even'
            elif current_status == 'even':
                new_status = 'odd'
            print('current_status:',current_status,'new_status:',new_status)
            if ((new_coordinates),new_status) not in squares_evaluated:
                squares_to_evaluate.append(((new_coordinates),new_status))
                squares_evaluated.append(((new_coordinates),new_status))
    print('step finished!')
print('finished!')

if number_of_steps % 2 == 0:
    criterion = 'even'
else:
    criterion = 'odd'
print('criterion:',criterion)

total = 0
for square_evaluated in squares_evaluated:
    print(square_evaluated[1])
    if square_evaluated[1] == criterion:
        total += 1
print('total:',total)
'''
testinput needs a number_of_steps of 6
testinput should give correct answer of 16

real input takes a number_of_steps of 64
correct answer for Part1 obtained: 3699
'''