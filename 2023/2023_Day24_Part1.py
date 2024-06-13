#!/usr/bin/env python3
#https://adventofcode.com/2023/day/24

folder = '2023/'
filename = '2023_Day24_testinput'
extension = '.txt'
full_path = folder + filename + extension
with open(full_path,'r') as file_object:
    file_content = file_object.readlines()
total = 0
positions_list = []
velocities_list = []
for line in file_content:
    line = line.strip()
    positions,velocities = line.split('@')
    positions = [int(str) for str in positions.split(',')]
    velocities = [int(str) for str in velocities.split(',')]
    positions_list.append(positions)
    velocities_list.append(velocities)

'''
Each hailstone path is a straight line which is a function of time.
Right now, the time is 0. The past refers to negative t.
Any t in the future should be included in the count of collisions, negative t should not be counted.
At a given time t, the x coordinate will be (px + (t * vx)) and y will be (py + (t * vy)).
If the paths are parallel the paths will never collide.
If the paths are not parallel then any two paths will collide once in the x,y plane.
'''
def count_intersections(positions_list,velocities_list):
    intersections_count = 0
    for i in range(len(positions_list)):
        px1,py1,pz1 = positions_list[i]
        vx1,vy1,vz1 = velocities_list[i]
        for j in range(i + 1,len(positions_list)):
            px2,py2,pz2 = positions_list[j]
            vx2,vy2,vz2 = positions_list[j]
            print(f'testing {positions_list[i]}{velocities_list[i]} against {positions_list[j]}{velocities_list[j]}') # should print 10 lines for testinput
    return intersections_count
total = count_intersections(positions_list,velocities_list)


print('total:',total)
test_dictionary = {
    '2023_Day24_input':
    {'attempts':(None),
    'low':None,'high':None,'answer':None},
    '2023_Day24_testinput':
    {'answer':2},
}

from testmodule import test_function
test_function(test_dictionary,filename,total)
'''


'''