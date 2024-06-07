#!/usr/bin/env python3
#https://adventofcode.com/2023/day/22

folder = '2023/'
filename = '2023_Day22_input'
extension = '.txt'
total = 0
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
    for brick in ordered_bricks_list:
        min_z = 1 # this still initialises the first brick in the ordered_bricks_list, which will be 1 anyway
        for previous_brick in recent_bricks:
            if intersects(previous_brick, brick):
                potential_z = z_heights[previous_brick] + (previous_brick[1][2] - previous_brick[0][2]) + 1
                if potential_z > min_z:
                    min_z = potential_z
        z_heights[brick] = min_z
        recent_bricks.append(brick)
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
    fallen_bricks_list = sorted(fallen_bricks_list, key=lambda x: int(x[0][2]))
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
#print('test_is_support (should be True for testinput): ',is_lower_support_of_higher(fallen_bricks_list[1],fallen_bricks_list[3]))

def process_supports_data(fallen_bricks_list):
    key_is_lower_dict = {}
    key_is_higher_dict = {}
    support_bricks = []
    for index, lower_brick in enumerate(fallen_bricks_list):
        is_lower_brick_support = False
        for higher_brick in fallen_bricks_list[index+1:]:
            if is_lower_support_of_higher(lower_brick, higher_brick):
                if lower_brick in key_is_lower_dict:
                    key_is_lower_dict[lower_brick].append(higher_brick)
                else:
                    key_is_lower_dict[lower_brick] = [higher_brick]
                is_lower_brick_support = True
                if higher_brick in key_is_higher_dict:
                    key_is_higher_dict[higher_brick].append(lower_brick)
                else:
                    key_is_higher_dict[higher_brick] = [lower_brick]
        if is_lower_brick_support:
            support_bricks.append(lower_brick)
    return key_is_lower_dict, key_is_higher_dict, support_bricks
key_is_lower_dict, key_is_higher_dict, support_bricks = process_supports_data(fallen_bricks_list)
'''
For each brick, how many other bricks would fall if that brick were disintegrated?
What is the sum of the number of other bricks that would fall?

Bricks which do not support other bricks will add 0 to the total.
'''
def cascade_bricks(base_brick, key_is_current_dict, key_is_next_dict):
    subtotal = 0
    queue = [base_brick]
    falling_bricks = set()
    while queue:
        current_brick = queue.pop(0)
        if current_brick not in key_is_current_dict:
            break
        for next_brick in key_is_current_dict[current_brick]:
            if key_is_next_dict[next_brick] == [current_brick]: # current brick is only support for next brick
                'add to falling bricks. add to queue'
                queue.append(next_brick)
                if next_brick not in falling_bricks:
                    falling_bricks.add(next_brick)
                    subtotal += 1
            else:
                if all(support in falling_bricks for support in key_is_next_dict[next_brick]): # all supports for next brick are falling.
                    'add to falling bricks. add to queue'
                    queue.append(next_brick)
                    if next_brick not in falling_bricks:
                        falling_bricks.add(next_brick)
                        subtotal += 1
    return subtotal
count = 0
for brick in support_bricks:
    count += 1
    print('brick number:',count) # number of support bricks is correct - matches Part1
    subtotal = cascade_bricks(brick,key_is_lower_dict, key_is_higher_dict) # per-brick total
    print(subtotal)
    total += subtotal

print('total:',total)
test_dictionary = {
    '2023_Day22_input':
    {'attempts':(None),
    'low':4641,'high':None,'answer':None},
    '2023_Day22_testinput':
    {'answer':7},
}

from testmodule import test_function
test_function(test_dictionary,filename,total)
'''

'''