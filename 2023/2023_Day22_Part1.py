#!/usr/bin/env python3
#https://adventofcode.com/2023/day/22

folder = '2023/'
filename = '2023_Day22_testinput'
extension = '.txt'
full_path = folder + filename + extension
total = 0
with open(full_path,'r') as file_object:
    file_content = file_object.readlines()
points_list = []
x_max = 0
y_max = 0
for line in file_content:
    point1 = tuple([int(item) for item in line.strip().split('~')[0].split(',')])
    point2 = tuple([int(item) for item in line.strip().split('~')[1].split(',')])
    if max(point1[0],point2[0]) > x_max:
        x_max = max(point1[0],point2[0])
    if max(point1[1],point2[1]) > y_max:
        y_max = max(point1[1],point2[1])
    points_list.append((point1,point2))
points_list = sorted(points_list, key=lambda x: int(x[1][2]))

x_length,y_length = x_max + 1,y_max + 1 # length includes 0
# points_list.insert(0,([0,0,0],[x_length,y_length,0]))
print('x_length:',x_length,', y_length:',y_length)

'''
x and y coordinates are relatively small. z is much larger in real input
'''

def intersects(brick1,brick2):
    b1_x_min = min(brick1[0][0],brick1[1][0])
    b1_x_max = max(brick1[0][0],brick1[1][0])
    b1_y_min = min(brick1[0][1],brick1[1][1])
    b1_y_max = max(brick1[0][1],brick1[1][1])
    b2_x_min = min(brick2[0][0],brick2[1][0])
    b2_x_max = max(brick2[0][0],brick2[1][0])
    b2_y_min = min(brick2[0][1],brick2[1][1])
    b2_y_max = max(brick2[0][1],brick2[1][1])
    
    if b1_x_max < b1_x_min or b2_x_max < b2_x_min or b1_y_max < b1_y_min or b2_y_max < b2_y_min:
        print('error!')
    '''
    print('b1_x_min' ,b1_x_min)
    print('b1_x_max' ,b1_x_max)
    print('b1_y_min' ,b1_y_min)
    print('b1_y_max' ,b1_y_max)
    print('b2_x_min' ,b2_x_min)
    print('b2_x_max' ,b2_x_max)
    print('b2_y_min' ,b2_y_min)
    print('b2_y_max' ,b2_y_max)'''

    if (b2_x_min <= b1_x_min <= b2_x_max) or (b2_x_min <= b1_x_max <= b2_x_max) or (b1_x_min <= b2_x_min <= b1_x_max) or (b1_x_min <= b2_x_max <= b1_x_max):
        if (b2_y_min <= b1_y_min <= b2_y_max) or (b2_y_min <= b1_y_max <= b2_y_max) or (b1_y_min <= b2_y_min <= b1_y_max) or (b1_y_min <= b2_y_max <= b1_y_max):
            return True
    return False
testb1 = ((1,2,3),(4,6,8))
testb2 = ((3,4,5),(3,5,7))
print('test for intersects:',intersects(testb1,testb2))

def return_min_z_heights():
    z_heights = {}
    recent_bricks = []
    for index,brick in enumerate(points_list):
        if index == 0:
            z_heights[brick] = 1
            recent_bricks.insert(0,brick)
            continue
        previous_brick = points_list[index - 1]
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