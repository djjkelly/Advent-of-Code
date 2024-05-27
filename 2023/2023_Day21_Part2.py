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
print('vertical_length:',vertical_length,'horizontal_length:',horizontal_length)
print(f'start point. line: {start_line} char: {start_char}')
'''
For part 2 I think I need to count the number of even and odd hashtags
I need to consider whether the starting point is even or odd (which means changing what even and odd means)
The numbers of lines and columns in the input data are both odd (131,131)
Most copies in this problem will be completely filled (in the middle of the copies)
Out of the filled copies, each will be either 'odd' or 'even'
The input start 'S' is located both in a blank column and row, so the propagation occurs linearly! (This is not true for the testinput)
the S position is also at (65,65) which is perfectly in the middle of our input ...
...meaning that new "copies" are encountered to the left, right, up, and down at the same rate
This also means that the path will always enter in the centre of the left, right, top, or bottom side of each new input copy

Considering first the copies in the right direction, the number of steps taken is 26501365.
65 steps are required to reach the edge of the original map in the right direction.
26501300 steps are taken outside the original map, meaning there are 202300 copies in left and right direction.
These "straight line" copies are filled along the middle line exactly to the end, but the last copy in up,down,left,right direction won't be completely filled.
This also means there are 202300 copies in the up and down direction, so there are 809200 copies in the four "+" direcions
The central copy is an "even copy", based on part 1. The map will fill out in this shape:
    X
   XXX
  XXXXX
 XXXXXXX
XXXXXXXXX
 XXXXXXX
  XXXXX
   XXX
    X
The number of copies not located on the perimeter is expressed by n(n-1) odd copies and n(n-1)+1 even copies.

'''
def is_in_bounds(new_coordinates):
    v,h = new_coordinates
    return 0 <= v <= vertical_length and 0 <= h <= horizontal_length

directions = {
    'down':(1,0),
    'right':(0,1),
    'up':(-1,0),
    'left':(0,-1)
}

number_of_steps = 26501365 # as per problem statement
copy_count = int((number_of_steps - start_char)/(horizontal_length + 1)) # this is the number of copies
print('copy_count:',copy_count)
steps_to_fully_fill = 132 # this will always be enough steps to fill a grid from the midpoint (= height//2 + width//2 + 2).

def fill_copy(start_line,start_char,even_or_odd,steps):
    squares_to_evaluate = [((start_line,start_char),even_or_odd)]
    squares_evaluated = [((start_line,start_char),even_or_odd)]
    for step_count in range(steps):
        current_squares_to_evaluate = copy.deepcopy(squares_to_evaluate)
        squares_to_evaluate = []
        while current_squares_to_evaluate:
            #print('\nNEW STEP! Current squares to evaluate:',current_squares_to_evaluate)
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
    print('fill_copy function finished!')
    even_plots_per_filled_copy = 0
    odd_plots_per_filled_copy = 0
    for square_evaluated in squares_evaluated:
        if square_evaluated[1] == 'even':
            even_plots_per_filled_copy += 1
        else:
            odd_plots_per_filled_copy += 1
    return even_plots_per_filled_copy,odd_plots_per_filled_copy

test_even,test_odd = fill_copy(65,65,'even',64)
print('should be 3699. test_even:',test_even) # should still be 3699 - and it is!

# this part calculates the total reachable plots for copies which are completely filled in
even_plots_per_filled_copy,odd_plots_per_filled_copy = fill_copy(start_line,start_char,'even',steps_to_fully_fill)
print('even per-copy:',even_plots_per_filled_copy,'odd per-copy:',odd_plots_per_filled_copy)
filled_copies_total = even_plots_per_filled_copy*((copy_count-1)**2) + odd_plots_per_filled_copy*(copy_count**2)
print('filled_copies_total:',filled_copies_total)

# this part calculates the partially filled copies at the farthest right, left, up, down points
right_point, unused_variable = fill_copy(65,0,'even',131) # the last input to fill_copy is 131 as the steps go right to the end of the last copy
left_point, unused_variable = fill_copy(65,130,'even',131)
top_point, unused_variable = fill_copy(0,65,'even',131)
bottom_point, unused_variable = fill_copy(130,65,'even',131)

print('right_point:',right_point,'left_point:',left_point,'top_point:',top_point,'bottom_point:',bottom_point)

total = filled_copies_total + right_point + left_point + top_point + bottom_point
print('intermediate total:',total)

'''I now need to consider the perimeter of the partially filled copies surrounding the diamond-shape of filled copies.
The perimeter of the diamond shape is 4 x copy_count
'''
top_right_even_edge, unused_variable = fill_copy(130,0,'even',196)
unused_variable, top_right_odd_edge = fill_copy(130,0,'odd',65)
top_left_even_edge, unused_variable = fill_copy(130,130,'even',196) # modified so that starting value is valid
unused_variable,top_left_odd_edge = fill_copy(130,130,'odd',65) # modified so that starting value is valid
bottom_right_even_edge, unused_variable = fill_copy(0,0,'even',196)
unused_variable, bottom_right_odd_edge = fill_copy(0,0,'odd',65)
bottom_left_even_edge, unused_variable = fill_copy(0,130,'even',196)
unused_variable, bottom_left_odd_edge = fill_copy(0,130,'odd',65)
print(f'top_right_even_edge: {top_right_even_edge},top_right_odd_edge: {top_right_odd_edge},  top_left_even_edge: {top_left_even_edge}, top_left_odd_edge: {top_left_odd_edge}')
print(f'bottom_right_even_edge: {bottom_right_even_edge}, bottom_right_odd_edge: {bottom_right_odd_edge}, bottom_left_even_edge: {bottom_left_even_edge}, bottom_left_odd_edge: {bottom_left_odd_edge}')

even_diagonals = (top_right_even_edge + top_left_even_edge + bottom_right_even_edge + bottom_left_even_edge) * (copy_count - 1)
odd_diagonals = (top_right_odd_edge + top_left_odd_edge + bottom_right_odd_edge + bottom_left_odd_edge) * (copy_count)
total += (even_diagonals + odd_diagonals)
print('grand total:',total)
if total == 602668853020498 or total == 602668880128698 or total == 613391353042289 or total == 613391300444549 or total == 613388299113968 or total == 613391342118089:
    print('answer incorrect - already submitted')
if total <= 602668880128698:
    print('answer incorrect - too low!')
if total >= 613391353042289:
    print('answer incorrect - too high!')

'''
real input takes a number_of_steps of 26501365
I need to double check whether the top, bottom, left and right are really even.
I think this makes sense as the middle (0) is even (excluded from copy count) and the 202300 is even too.

602668853020498 incorrect - answer too low!
602668880128698 incorrect - answer too low!
613391353042289 incorrect - answer too high!
613391300444549 incorrect
613388299113968 incorrect
613391342118089 incorrect
'''