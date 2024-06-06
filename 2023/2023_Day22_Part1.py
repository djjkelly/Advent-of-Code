#!/usr/bin/env python3
#https://adventofcode.com/2023/day/22

folder = '2023/'
filename = '2023_Day22_testinput'
extension = '.txt'
full_path = folder + filename + extension
total = 0
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
            print(f'brick intersection found between {previous_brick} and {brick}')
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
Now I need to calculate how many supports each brick has.
A higher brick (brick1) is supported by a lower brick (brick2) if:
- The bricks intersect
- z_min of upper brick == z_max of lower brick + 1
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

def is_lower_support_of_higher(lower_brick,higher_brick): # accepts the original brick tuples
    if intersects(higher_brick,lower_brick):
        if higher_brick[0][2] == lower_brick[1][2] + 1:
            return True
    return False
print('test_is_support (should be True): ',is_lower_support_of_higher(fallen_bricks_list[1],fallen_bricks_list[3]))

def count_blocks_supporting_each_brick(fallen_bricks_list):
    supporting_counts_per_brick = {}
    for index,brick in enumerate(fallen_bricks_list):
        number_supporting = 0
        for check_brick in fallen_bricks_list[index+1:]:
            if is_lower_support_of_higher(lower_brick = brick, higher_brick = check_brick):
                number_supporting += 1
        supporting_counts_per_brick[brick] = number_supporting
        print(number_supporting)
    return supporting_counts_per_brick
supporting_counts = count_blocks_supporting_each_brick(fallen_bricks_list)

print('total:',total)
test_dictionary = {
    '2023_Day22_input':
    {'attempts':(None),
    'low':None,'high':None,'answer':None},
    '2023_Day22_testinput':
    {'answer':5},
}

from testmodule import test_function
test_function(test_dictionary,filename,total)
'''
There are about 1500 bricks, about 10 x 10 x 300 cube.
'''