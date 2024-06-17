#!/usr/bin/env python3
#https://adventofcode.com/2023/day/24

from sympy import symbols, Eq, solve

folder = '2023/'
filename = '2023_Day24_input'
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

'''
def count_intersections(positions_list,velocities_list):
    intersections_count = 0
    for i in range(len(positions_list)):
        px1,py1,_ = positions_list[i]
        vx1,vy1,_ = velocities_list[i]
        g1 = vy1/vx1
        for j in range(i + 1,len(positions_list)):
            px2,py2,_ = positions_list[j]
            vx2,vy2,_ = velocities_list[j]
            g2 = vy2/vx2
            print(f'testing {positions_list[i]}{velocities_list[i]}, gradient {g1},     against {positions_list[j]}{velocities_list[j]}, gradient {g2}')
            if g1 == g2:
                print('lines parralel, skipping this comparison')
                continue # not added to count
            t2 = ( ( px1 * vy1 ) - ( px2 * vy1 ) + ( py2 * vx1 ) - ( py1 * vx1 ) ) / ( ( vx2 * vy1 ) - ( vy2 * vx1 ) )
            ix = px2 + (t2 * vx2)
            iy = py2 + (t2 * vy2)
            t1 = ( ix - px1 ) / vx1
            ti = min(t1,t2) # time at first intersection
            if 200000000000000 <= ix <= 400000000000000 and 200000000000000 <= iy <= 400000000000000:
                if ti > 0:
                    intersections_count +=1
                else:
                    print('happened in the past!')
            else:
                print('outside grid!')
    return intersections_count
total = count_intersections(positions_list,velocities_list)


print('total:',total)
test_dictionary = {
    '2023_Day24_input':
    {'attempts':(None),
    'low':None,'high':None,'answer':None},
    '2023_Day24_testinput':
    {'answer':47},
}

from testmodule import test_function
test_function(test_dictionary,filename,total)
'''


'''