#!/usr/bin/env python3
#https://adventofcode.com/2023/day/24

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
for path 1 and path 2 the lines are...      note that t is not the same, as the paths may cross at different times.
ix1 = px1 + (t1 * vx1)                                              iy1 = py1 + (t1 * vy1)
ix2 = px2 + (t2 * vx2)                                              iy2 = py2 + (t2 * vy2)
equating ix1 = ix2...                       intersect is the same for both lines
px1 + ( t1 * vx1 ) = px2 + ( t2 * vx2 )                             py1 + ( t1 * vy1 ) = py2 + ( t2 * vy2 )
( t1 * vx1 ) = px2 + ( t2 * vx2 ) -  px1                            ( t1 * vy1 ) = py2 + ( t2 * vy2 ) -  py1
t1 = ( px2 + ( t2 * vx2 ) -  px1 ) / vx1                            t1 = ( py2 + ( t2 * vy2 ) -  py1 ) / vy1
substituting t1 into the formula for ix1...                         and iy1...
ix1 = px1 + ( ( ( px2 + ( t2 * vx2 ) -  px1 ) / vx1) * vx1 )        iy1 = py1 + ( ( ( py2 + ( t2 * vy2 ) -  py1 ) / vy1) * vy1 )
ix1 = px1 + px2 + ( t2 * vx2 ) -  px1                               iy1 = py1 + py2 + ( t2 * vy2 ) -  py1
ix1 = px2 + ( t2 * vx2 )                                            iy1 = py2 + ( t2 * vy2 )
t2 formulae will be...
t2 = ( px1 + ( t1 * vx1 ) -  px2 ) / vx2                            t2 = ( py1 + ( t1 * vy1 ) -  py2 ) / vy2
substituting t2 into the formula for ix2...                         and iy2...
ix2 = px2 + ( ( ( px1 + ( t1 * vx1 ) -  px2) / vx2 ) * vx2 )        iy2 = py2 + ( ( (py1 + ( t1 * vy1 ) -  py2 ) / vy2 ) * vy2 )
ix2 = px2 + px1 + ( t1 * vx1 ) - px2                                iy2 = py2 + py1 + ( t1 * vy1 ) - py2
ix2 = px1 + ( t1 * vx1 )                                            iy2 = py1 + ( t1 * vy1 )
set ix1 = ix2 and iy1 = iy2...
px2 + ( t2 * vx2 ) = px1 + ( t1 * vx1 )                             py1 + ( t1 * vy1 ) = py2 + ( t2 * vy2 )
( t2 * vx2 ) = px1 + ( t1 * vx1 ) - px2                             ( t1 * vy1 ) = py2 + ( t2 * vy2 ) - py1
t2 = ( px1 + ( t1 * vx1 ) - px2 ) / vx2                             t1 = ( py2 + ( t2 * vy2 ) - py1 ) / vy1
combining...
t2 = ( px1 + ( ( ( py2 + ( t2 * vy2 ) - py1 ) / vy1 ) * vx1 ) - px2 ) / vx2                     checked to here, this seems correct
multiply both sides by vx2...
( t2 * vx2 ) = px1 + ( ( ( py2 + ( t2 * vy2 ) - py1 ) / vy1 ) * vx1 ) - px2
rearranging...
( t2 * vx2 ) = px1 - px2 + ( ( py2 + ( t2 * vy2 ) - py1 ) * vx1 ) ) / vy1
multiply both sides by vy1...
( t2 * vx2 * vy1 ) = ( px1 * vy1 ) - ( px2 * vy1 ) + ( ( py2 + ( t2 * vy2 ) - py1 ) * vx1 ) )
multiply out...
( t2 * vx2 * vy1 ) = ( px1 * vy1 ) - ( px2 * vy1 ) + ( py2 * vx1 ) + ( ( t2 * vy2 ) * vx1 ) - ( py1 * vx1 )
rearranging...
( t2 * vx2 * vy1 ) = ( px1 * vy1 ) - ( px2 * vy1 ) - ( py2 * vx1 ) + ( py1 * vx1 ) + ( t2 * vy2 * vx1 )
( t2 * vx2 * vy1 ) - ( t2 * vy2 * vx1 ) = ( px1 * vy1 ) - ( px2 * vy1 ) + ( py2 * vx1 ) - ( py1 * vx1 )
factorise...
t2 * ( ( vx2 * vy1 ) - ( vy2 * vx1 ) ) = ( px1 * vy1 ) - ( px2 * vy1 ) + ( py2 * vx1 ) - ( py1 * vx1 )
rearrange...
t2 = ( ( px1 * vy1 ) - ( px2 * vy1 ) + ( py2 * vx1 ) - ( py1 * vx1 ) ) / ( ( vx2 * vy1 ) - ( vy2 * vx1 ) )

to calculate t1...
ix1 = px1 + (t1 * vx1)
ix1 - px1 = t1 * vx1
t1 = ( ix1 - px1 ) / vx1
t1 = ( ix - px1 ) / vx1


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
    'low':None,'high':None,'answer':19523},
    '2023_Day24_testinput':
    {'answer':2},
}

from testmodule import test_function
test_function(test_dictionary,filename,total)
'''


'''