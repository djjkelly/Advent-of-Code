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

x = px + (t * vx)
y = py + (t * vy)
let's call the intersect points ix and iy
ix = px + (t * vx)
iy = py + (t * vy)
rearranging the x equation...
t = ( ix - px ) / vx
this applies for 1 and 2. combining...
( ix - px1 ) / vx1 = ( ix - px2 )/ vx2
rearranging...
( ix - px1 ) * vx2 = ( ix - px2 ) * vx1

rearranging...
( ix - px1 ) / ( ix - px2 ) = vx1 / vx2
similarly for y...
( iy - py1 ) / ( iy - py2 ) = vy1 / vy2
let...
    dvx = vx1 / vx2
    dvy = vy1 / vy2
input dvx, dvy...
( ix - px1 ) / ( ix - px2 ) = dvx
( iy - py1 ) / ( iy - py2 ) = dvy
rearranging...
( ix - px1 ) = dvx * ( ix - px2 )
( iy - py1 ) = dvy * ( iy - py2 )
expanding...
ix - px1 = ( dvx * ix ) - ( dvx * px2 )
iy - py1 = ( dvy * iy ) - ( dvy * py2 )
rearranging...
ix = ( dvx * ix ) - ( dvx * px2 ) - px1
iy = ( dvy * iy ) - ( dvy * py2 ) - py1
rearranging...
( dvx * ix ) - ix = ( dvx * px2 ) + px1
( dvy * iy ) - iy = ( dvy * py2 ) + py1
expanding...
ix * ( dvx - 1 ) = ( dvx * px2 ) + px1
iy * ( dvy - 1 ) = ( dvy * py2 ) + py1
rearranging...
ix  = (( dvx * px2 ) + px1 ) / ( dvx - 1 )
iy  = (( dvy * py2 ) + py1 ) / ( dvy - 1 )

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
            dvx = vx1 / vx2 # = ( ix - px1 ) / ( ix - px2 )
            dvy = vy1 / vy2 # = ( iy - py1 ) / ( iy - py2 )
            print('dvx:',dvx,' dvy:',dvy)
            ix  = (( dvx * px2 ) + px1 ) / ( dvx - 1 )
            iy  = (( dvy * py2 ) + py1 ) / ( dvy - 1 )
            if 7 <= ix <= 27 and 7 <= iy <= 27:
                intersections_count +=1
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
    {'answer':2},
}

from testmodule import test_function
test_function(test_dictionary,filename,total)
'''


'''