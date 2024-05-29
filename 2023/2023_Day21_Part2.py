#!/usr/bin/env python3
#https://adventofcode.com/2023/day/21

folder = '2023/'
filename = '2023_Day21_input'
extension = '.txt'
full_path = folder + filename + extension

with open(full_path,'r') as file_object:
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
The starting point is even, meaning an even number of steps (0 steps) from the start position (65,65).
The numbers of lines and columns in the input data are both odd (131,131)
Most copies in this problem will be completely filled (in the middle of the copies)
Out of the filled copies, each will be either 'odd' or 'even' (the start point will have taken)
The input start 'S' is located both in a blank column and row, so the propagation occurs linearly! (This is not true for the testinput which is now worthless)
the S position (65,65) is perfectly in the middle of our input ...
...meaning that new "copies" are encountered to the left, right, up, and down at the same rate (after 65 steps the first time, after 131 steps thereafter)
This also means that the path will always enter in the centre of the left, right, top, or bottom side of each filled input copy

Considering first the copies in the right direction, the number of steps taken is 26501365.
65 steps are required to reach the edge of the original map in the right direction.
26501300 steps are taken outside the original map, meaning there are (26501300/131=) 202300 copies in left and right direction.
These "straight line" copies are filled along the middle line exactly to the end, but the last copy in up,down,left,right direction won't be completely filled.
This also means there are 202300 copies in the up and down direction, so there are 809200 copies in the four "+" direcions
The central copy is an "even copy", based on the approach in Part 1. The map will fill out in this shape:
        X
      X X X
    X X X X X
  X X X X X X X 
X X X X X X X X X
  X X X X X X X
    X X X X X
      X X X
        X
The number of copies not located on the perimeter is expressed by (n-1)^2 even copies and n^2 odd copies.
Because the ends are even, there are a larger number of completely filled odd copies compared to even copies.

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

def fill_copy(start_line, start_char, even_or_odd, steps):
    squares_to_evaluate = { (start_line, start_char): even_or_odd }
    squares_evaluated = {}  # Use a dictionary to track all evaluated coordinates and their statuses
    for step_count in range(steps):
        current_squares_to_evaluate = squares_to_evaluate.copy()
        squares_to_evaluate = {}
        for current_coordinates, current_status in current_squares_to_evaluate.items():
            for direction, move in directions.items():
                new_coordinates = (current_coordinates[0] + move[0], current_coordinates[1] + move[1])
                #print('direction:', direction, ', move:', move)
                #print('current_coordinates:', current_coordinates, ' new_coordinates:', new_coordinates)
                if is_in_bounds(new_coordinates) and input_list[new_coordinates[0]][new_coordinates[1]] != '#':
                    if current_status == 'odd':
                        new_status = 'even'
                    elif current_status == 'even':
                        new_status = 'odd'
                    #print('current_status:', current_status, 'new_status:', new_status)
                    if new_coordinates not in squares_evaluated:
                        squares_to_evaluate[new_coordinates] = new_status
                        squares_evaluated[new_coordinates] = new_status
                        #print('Adding new coordinate to evaluate:', new_coordinates, 'with status:', new_status)
        #print('step finished!')
    print('fill_copy function finished!')
    even_plots_per_filled_copy = 0
    odd_plots_per_filled_copy = 0
    for coordinates, status in squares_evaluated.items():
        if status == 'even':
            even_plots_per_filled_copy += 1
        else:
            odd_plots_per_filled_copy += 1
    return even_plots_per_filled_copy, odd_plots_per_filled_copy

test_even,test_odd = fill_copy(65,65,'even',64) # why is the answer for 64 the same as 65? Is this because of the blank row around the edge?
print('should be 3699. test_even:',test_even) # should still be 3699 - and it is!

# this part calculates the total reachable plots for copies which are completely filled in
even_plots_per_filled_copy,odd_plots_per_filled_copy = fill_copy(start_line,start_char,'even',steps_to_fully_fill)
print('even per-copy:',even_plots_per_filled_copy,'odd per-copy:',odd_plots_per_filled_copy)
filled_copies_total = even_plots_per_filled_copy*((copy_count-1)**2) + odd_plots_per_filled_copy*(copy_count**2)
print('filled_copies_total:',filled_copies_total)

# this part calculates the partially filled copies at the farthest right, left, up, down points
right_point, unused_variable = fill_copy(65,0,'even',130) # the last input to fill_copy is 131 as the steps go right to the end of the last copy
left_point, unused_variable = fill_copy(65,130,'even',130)
top_point, unused_variable = fill_copy(0,65,'even',130)
bottom_point, unused_variable = fill_copy(130,65,'even',130) # using 130 and 131 as the step number give the exact same result (?)

print('right_point:',right_point,'left_point:',left_point,'top_point:',top_point,'bottom_point:',bottom_point)
total = filled_copies_total + right_point + left_point + top_point + bottom_point
print('intermediate total:',total)

# calculation for odd and even copies on the diagonals:
top_right_even_edge, unused_variable = fill_copy(130,0,'even',196) # 196 and 195 give different answers
unused_variable, top_right_odd_edge = fill_copy(130,0,'odd',65) # 64 and 65 give the same answers
top_left_even_edge, unused_variable = fill_copy(130,130,'even',196)
unused_variable,top_left_odd_edge = fill_copy(130,130,'odd',65)
bottom_right_even_edge, unused_variable = fill_copy(0,0,'even',196)
unused_variable, bottom_right_odd_edge = fill_copy(0,0,'odd',65)
bottom_left_even_edge, unused_variable = fill_copy(0,130,'even',196)
unused_variable, bottom_left_odd_edge = fill_copy(0,130,'odd',65)
print(f'top_right_even_edge: {top_right_even_edge},top_right_odd_edge: {top_right_odd_edge},  top_left_even_edge: {top_left_even_edge}, top_left_odd_edge: {top_left_odd_edge}')
print(f'bottom_right_even_edge: {bottom_right_even_edge}, bottom_right_odd_edge: {bottom_right_odd_edge}, bottom_left_even_edge: {bottom_left_even_edge}, bottom_left_odd_edge: {bottom_left_odd_edge}')

even_diagonals = (top_right_even_edge + top_left_even_edge + bottom_right_even_edge + bottom_left_even_edge) * (copy_count - 1)
odd_diagonals = (top_right_odd_edge + top_left_odd_edge + bottom_right_odd_edge + bottom_left_odd_edge) * (copy_count)
total += (even_diagonals + odd_diagonals)

test_dictionary = {
    '2023/2023_Day21_input.txt':{'attempts':(613391300444549,613388299113968,613391342118089,613391289520349),
    'low':602668880128698,'high':613391353042289,'answer':None},
}

from testmodule import test_function
test_function(test_dictionary,full_path,total)
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
613391289520349 incorrect
'''