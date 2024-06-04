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
    point1 = [int(item) for item in line.strip().split('~')[0].split(',')]
    point2 = [int(item) for item in line.strip().split('~')[1].split(',')]
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

def is_in_vertical_line(x,y,brick):
    x_min = min(brick[0][0],brick[1][0])
    x_max = max(brick[0][0],brick[1][0])
    y_min = min(brick[0][1],brick[1][1])
    y_max = max(brick[0][1],brick[1][1])
    if x_min <= x <= x_max:
        if y_min <= y <= y_max:
            return True
    return False

dependencies_map = [[[] for _ in range(y_length)] for _ in range(x_length)]
def fill_dependencies_map(dependencies_map):
    for x in range(x_length):
        for y in range(y_length):
            for brick in points_list:
                if is_in_vertical_line(x,y,brick):
                    print('brick found in vertical')
                    if brick not in dependencies_map[x][y]:
                        dependencies_map[x][y].append(brick)
    return dependencies_map
dependencies_map = fill_dependencies_map(dependencies_map)
print(dependencies_map[0][0])

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