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
total = 0
'''
The starting point (0,0) starts off even, but after an odd number of steps it will not be one of the possibilities.
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
The central copy is an "odd copy", due to the odd number of steps in Part2. The map will fill out in this shape:
        X
      X X X
    X X X X X
  X X X X X X X 
X X X X X X X X X
  X X X X X X X
    X X X X X
      X X X
        X
The number of copies not located on the perimeter is expressed by (n-1)^2 odd copies and n^2 even copies.
Because the ends are even, there are a larger number of completely filled even copies compared to odd copies.

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
steps_to_fully_fill = 130 # this will always be enough steps to fill a grid from the midpoint (= height//2 + width//2).

def fill_copy(start_line, start_char, even_or_odd_copy, steps):
    if (start_line % 2 == 0) == (start_char % 2 == 0):
        even_or_odd_start = 'even'
    else:
        even_or_odd_start = 'odd'

    squares_to_evaluate = { (start_line, start_char): even_or_odd_start }
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
    plots_per_filled_copy = 0
    for coordinates, status in squares_evaluated.items():
        if status == even_or_odd_copy:
            plots_per_filled_copy += 1
    return plots_per_filled_copy

test_even = fill_copy(65,65,'even',64)
if test_even == 3699:
    print('TEST PASSED! 3699 condition met')

# this part calculates the total reachable plots for copies which are completely filled in
count_for_odd_copies = fill_copy(start_line,start_char,'odd',130)
counts_for_even_copies = fill_copy(start_line,start_char,'even',130) # 130 is the amount of moves needed to fill the end, not 131! (130 and 132 give same answer, meaning it's full)

# an 'odd copy' is one where the 65,65 point will be counted on an even number of steps (i.e. it matches the original map).
# an 'odd square' which will be counted on an odd number of steps (like 65,66 in the original map, or 65,65 in the 4 next (even) copies).
# an 'even copy' is one where the 65,65 point will be counted on an odd number of steps

number_of_odd_filled_copies = (copy_count - 1) ** 2
number_of_even_filled_copies = (copy_count) ** 2

filled_copies_total = (count_for_odd_copies * number_of_odd_filled_copies) + (counts_for_even_copies * number_of_even_filled_copies)
print('even per-copy:',count_for_odd_copies,'odd per-copy:',counts_for_even_copies)
print('filled_copies_total:',filled_copies_total)

# this part calculates the partially filled copies at the farthest right, left, up, down points
right_point = fill_copy(65,0,'odd',130) # the last input to fill_copy is 131 as the steps go right to the end of the last copy
left_point = fill_copy(65,130,'odd',130)
top_point = fill_copy(0,65,'odd',130)
bottom_point = fill_copy(130,65,'odd',130)

print('right_point:',right_point,'left_point:',left_point,'top_point:',top_point,'bottom_point:',bottom_point)
total = filled_copies_total + right_point + left_point + top_point + bottom_point
print('intermediate total:',total)

# calculation for odd and even copies on the diagonals:
top_right_big_edge = fill_copy(130,0,'odd',195) # big edges should be odd
top_right_small_edge = fill_copy(130,0,'even',65) # small edges should be even
top_left_big_edge = fill_copy(130,130,'odd',195)
top_left_small_edge = fill_copy(130,130,'even',65)
bottom_right_big_edge = fill_copy(0,0,'odd',195)
bottom_right_small_edge = fill_copy(0,0,'even',65)
bottom_left_big_edge = fill_copy(0,130,'odd',195)
bottom_left_small_edge = fill_copy(0,130,'even',65)
print(f'top_right_big_edge: {top_right_big_edge}, top_right_odd_edge: {top_right_small_edge},  top_left_big_edge: {top_left_big_edge}, top_left_small_edge: {top_left_small_edge}')
print(f'bottom_right_big_edge: {bottom_right_big_edge}, bottom_right_small_edge: {bottom_right_small_edge}, bottom_left_big_edge: {bottom_left_big_edge}, bottom_left_small_edge: {bottom_left_small_edge}')

big_diagonals = (top_right_big_edge + top_left_big_edge + bottom_right_big_edge + bottom_left_big_edge) * (copy_count - 1)
small_diagonals = (top_right_small_edge + top_left_small_edge + bottom_right_small_edge + bottom_left_small_edge) * (copy_count)
total += (big_diagonals + small_diagonals)

test_dictionary = {
    '2023/2023_Day21_input.txt':
    {'attempts':(613391300444549,613388299113968,613391342118089,613391289520349,613391299230782,613391321079128,613391268076632,613391289925448,613391289924978),
    'low':602668880128698,'high':613391353042289,'answer':613391294577878},
}
print('total:',total)

from testmodule import test_function
test_function(test_dictionary,full_path,total)
'''
real input takes a number_of_steps of 26501365
top, bottom, left and right (as on the +) are odd copies.
This is because they are an even number of copies away from the original map, but the number of steps is odd.

602668853020498 incorrect - answer too low!
602668880128698 incorrect - answer too low!
613391353042289 incorrect - answer too high!
613391300444549 incorrect
613388299113968 incorrect
613391342118089 incorrect
613391289520349 incorrect
613391299230782 incorrect - new approach to odd and even.
613391321079128 incorrect
613391268076632 incorrect
613391289925448 incorrect
613391289924978 incorrect
'''