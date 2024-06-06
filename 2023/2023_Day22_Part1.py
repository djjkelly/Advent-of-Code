#!/usr/bin/env python3
#https://adventofcode.com/2023/day/22

folder = '2023/'
filename = '2023_Day22_input'
extension = '.txt'
full_path = folder + filename + extension
with open(full_path,'r') as file_object:
    file_content = file_object.readlines()
ordered_bricks_list = []
x_max = 0
y_max = 0
for line in file_content:
    point1 = tuple([int(item) for item in line.strip().split('~')[0].split(',')])
    point2 = tuple([int(item) for item in line.strip().split('~')[1].split(',')])
    if max(point1[0],point2[0]) > x_max:
        x_max = max(point1[0],point2[0])
    if max(point1[1],point2[1]) > y_max:
        y_max = max(point1[1],point2[1])
    ordered_bricks_list.append((point1,point2))
ordered_bricks_list = sorted(ordered_bricks_list, key=lambda x: int(x[0][2]))

x_length,y_length = x_max + 1,y_max + 1 # length includes 0
# points_list.insert(0,([0,0,0],[x_length,y_length,0]))
print('x_length:',x_length,', y_length:',y_length)

'''
x and y coordinates are relatively small. z is much larger in real input
'''

def intersects(brick1,brick2):
    b1_x_min = brick1[0][0]
    b1_x_max = brick1[1][0]
    b1_y_min = brick1[0][1]
    b1_y_max = brick1[1][1]
    b2_x_min = brick2[0][0]
    b2_x_max = brick2[1][0]
    b2_y_min = brick2[0][1]
    b2_y_max = brick2[1][1]
    # if the coordinate is different, the larger number is always at brick[1]
    if b1_x_max < b1_x_min or b2_x_max < b2_x_min or b1_y_max < b1_y_min or b2_y_max < b2_y_min:
        print('error!')

    if (b2_x_min <= b1_x_min <= b2_x_max) or (b2_x_min <= b1_x_max <= b2_x_max) or (b1_x_min <= b2_x_min <= b1_x_max) or (b1_x_min <= b2_x_max <= b1_x_max):
        if (b2_y_min <= b1_y_min <= b2_y_max) or (b2_y_min <= b1_y_max <= b2_y_max) or (b1_y_min <= b2_y_min <= b1_y_max) or (b1_y_min <= b2_y_max <= b1_y_max):
            return True
    return False
testb1 = ((1,2,3),(4,6,8))
testb2 = ((3,4,5),(3,5,7))
print('test for intersects (should be true):',intersects(testb1,testb2))

def return_min_z_heights():
    z_heights = {}
    recent_bricks = []
    for index,brick in enumerate(ordered_bricks_list):
        if index == 0:
            z_heights[brick] = 1
            recent_bricks.insert(0,brick)
            continue
        previous_brick = ordered_bricks_list[index - 1]
        if intersects(previous_brick,brick):
            z_heights[brick] = z_heights[previous_brick] + 1
            recent_bricks.insert(0,brick)
        else:
            for previous_brick in recent_bricks:
                if intersects(previous_brick,brick):
                    z_heights[brick] = z_heights[previous_brick] + 1
                    recent_bricks.insert(0,brick)
                    break
                else:
                    z_heights[brick] = 1
    return z_heights
min_z_heights = return_min_z_heights()

'''
min_z_heights looks correct for test data.
I want to drop the bricks to their final z positions (all coordinates final)
'''

def drop_bricks_to_final_z_positions(ordered_bricks_list,min_z_heights):
    fallen_bricks_list = []
    for brick in ordered_bricks_list:
        new_z_min = min_z_heights[brick]
        if brick[1][2] > brick [0][2]:
            new_z_max = new_z_min + brick[1][2] - brick [0][2]
        else:
            new_z_max = new_z_min
        new_brick = ((brick[0][0],brick[0][1],new_z_min),(brick[1][0],brick[1][1],new_z_max))
        fallen_bricks_list.append(new_brick)
    fallen_bricks_list = sorted(fallen_bricks_list, key=lambda x: int(x[0][2])) # sorting by z again - is this necessary? Do we want sorted by max or min?
    return fallen_bricks_list
fallen_bricks_list = drop_bricks_to_final_z_positions(ordered_bricks_list,min_z_heights)

'''
Now I need to calculate how many supports each brick has.
A higher brick (brick1) is supported by a lower brick (brick2) if:
- The bricks intersect
and
- z_min of upper brick == z_max of lower brick + 1
'''

def is_lower_support_of_higher(lower_brick,higher_brick): # accepts the original brick tuples
    if intersects(higher_brick,lower_brick):
        if higher_brick[0][2] == lower_brick[1][2] + 1:
            return True
    return False
#print('test_is_support (should be True): ',is_lower_support_of_higher(fallen_bricks_list[1],fallen_bricks_list[3]))

'''
If a brick is not supporting another brick, it can be disintegrated.
When a brick is supporting another brick, it can only be disintegrated if all the bricks it's supporting are supported by at least one other brick.
'''

def count_blocks_supporting_each_brick(fallen_bricks_list):
    higher_bricks_being_supported_by_each_brick = {}
    number_of_bricks_not_supporting_other_bricks = 0
    for index,brick in enumerate(fallen_bricks_list):
        higher_bricks_supported = []
        for higher_brick in fallen_bricks_list[index+1:]:
            if is_lower_support_of_higher(lower_brick = brick, higher_brick = higher_brick):
                #print('True for lower brick',brick,'higher brick ',check_brick)
                higher_bricks_supported.append(higher_brick)
        if higher_bricks_supported == []:
            number_of_bricks_not_supporting_other_bricks += 1
        else:
            higher_bricks_being_supported_by_each_brick[brick] = higher_bricks_supported
    return higher_bricks_being_supported_by_each_brick , number_of_bricks_not_supporting_other_bricks
higher_bricks_being_supported_by_each_brick, total = count_blocks_supporting_each_brick(fallen_bricks_list)

'''
Now I need to consider the bricks which are supporting other bricks
'''

def iterate_supporting_counts(higher_bricks_being_supported):
    count = 0
    values = higher_bricks_being_supported.values()
    # aims to count the number of times each higher_brick appears in the values()
    for higher_bricks in values:
        can_be_disintegrated = True
        for higher_brick in higher_bricks:
            if sum(sublist.count(higher_brick) for sublist in values) <= 1:
                can_be_disintegrated = False
        if can_be_disintegrated:
            count += 1
    return count
total += iterate_supporting_counts(higher_bricks_being_supported_by_each_brick)

print('total:',total)
test_dictionary = {
    '2023_Day22_input':
    {'attempts':(None),
    'low':464,'high':670,'answer':None},
    '2023_Day22_testinput':
    {'answer':5},
}

from testmodule import test_function
test_function(test_dictionary,filename,total)
'''
There are about 1500 bricks, about 10 x 10 x 300 cube.
incorrect answer 670 - answer too high
I'm confident that the right answer is above 464.
464 is the number of bricks which aren't supporting any other bricks.
'''