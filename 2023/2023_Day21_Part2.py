#!/usr/bin/env python3
#https://adventofcode.com/2023/day/21

import copy

with open("2023/2023_Day21_testinput.txt",'r') as file_object:
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
print('vertical_length:',vertical_length,'horizontal_length:',horizontal_length)
print(f'start point. line: {start_line} char: {start_char}')
'''
For part 2 I think I need to count the number of even and odd hashtags
I need to consider whether the starting point is even or odd (which means changing what even and odd means)
The numbers of lines and columns in the input data are both even (130 each)
However I don't know how to account for how quickly each step propagates towards the next copy of the input
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
numbers_of_steps = [6,10,50,100,500,1000,5000]

for number_of_steps in numbers_of_steps:
    #number_of_steps = 26501365
    step_count = 0
    squares_to_evaluate = [((start_line,start_char),'even')]
    squares_evaluated = [((start_line,start_char),'even')]
    for step_count in range(number_of_steps):
        current_squares_to_evaluate = copy.deepcopy(squares_to_evaluate)
        squares_to_evaluate = []
        while current_squares_to_evaluate:
            #print('\nNEW STEP! Current squares to evaluate:\n',current_squares_to_evaluate)
            current_square = current_squares_to_evaluate.pop(0)
            current_coordinates = current_square[0]
            current_status = current_square[1]
            for directions_item in directions.items():
                direction,move = directions_item[0],directions_item[1]
                #print('direction:', direction, ', move:', move)
                new_coordinates = tuple(x+y for x,y in zip(current_coordinates,move))
                #print('current_coordinates:',current_coordinates,' new_coordinates:',new_coordinates)
                if not is_in_bounds(new_coordinates):
                    #print('out of bounds!')
                    continue
                if input_list[new_coordinates[0]][new_coordinates[1]] == '#':
                    #print('hashtag found in direction',direction,'ignoring this square')
                    continue
                if current_status == 'odd':
                    new_status = 'even'
                elif current_status == 'even':
                    new_status = 'odd'
                #print('current_status:',current_status,'new_status:',new_status)
                if ((new_coordinates),new_status) not in squares_evaluated:
                    squares_to_evaluate.append(((new_coordinates),new_status))
                    squares_evaluated.append(((new_coordinates),new_status))
        #print('step finished!')
    print('finished!')
    if number_of_steps % 2 == 0:
        criterion = 'even'
    else:
        criterion = 'odd'
    print('number_of_steps:',number_of_steps,' criterion:',criterion)
    total = 0
    for square_evaluated in squares_evaluated:
        if square_evaluated[1] == criterion:
            total += 1
    print('total:',total)
'''
testinput with 6 steps should give an answer of 16
testinput with 10 steps should give an answer of 50
testinput with 50 steps should give an answer of 1594
testinput with 100 steps should give an answer of 6536
testinput with 500 steps should give an answer of 167004
testinput with 1000 steps should give an answer of 668697
testinput with 5000 steps should give an answer of 16733044

real input takes a number_of_steps of 26501365

using a single copy of the real input the computation does eventually finish and gives an answer of 7336.
However, using the "infinite copies" this computation will be much longer as squares_to_evaluate won't already appear in squares_evaluated.
'''