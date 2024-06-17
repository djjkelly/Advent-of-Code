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
I think we only need to look at 3 points to figure out the starting position and velocity.
Start positions x3 and velocities x3 need to be taken into account.
t represents the time of the actual impact (for each hailstone)
rock_start_x = px + (t * (rock_start_vx - vx)      or      t = ( rock_start_x - px ) / (rock_start_vx - vx)
rock_start_y = py + (t * (rock_start_vy - vy)      or      t = ( rock_start_y - py ) / (rock_start_vy - vy)
rock_start_z = pz + (t * (rock_start_vz - vz)      or      t = ( rock_start_z - pz ) / ( rock_start_vz - vz)

eliminate t as we are calculating start values...
( rock_start_x - px ) / ( rock_start_vx - vx ) = ( y - py ) / ( rock_start_vy - vy )
( rock_start_y - py ) / ( rock_start_vy - vy ) = ( z - pz ) / ( rock_start_vz - vz )

rewritten...
( rock_start_vy - vy ) * ( rock_start_x - px ) = ( rock_start_vx - vx ) * ( rock_start_y - py )
( rock_start_vz - vz ) * ( rock_start_y - py ) =  ( rock_start_vy - vy) * ( rock_start_z - pz )
or with a comma instead of '='...
( rock_start_vy - vy ) * ( rock_start_x - px ), ( rock_start_vx - vx ) * ( rock_start_y - py )
( rock_start_vz - vz ) * ( rock_start_y - py ),  ( rock_start_vy - vy) * ( rock_start_z - pz )

'''
def count_intersections(positions_list,velocities_list):
    equations = []
    rock_start_x,rock_start_y,rock_start_z,rock_start_vx,rock_start_vy,rock_start_vz = symbols('rock_start_x, rock_start_y, rock_start_z, rock_start_vx, rock_start_vy, rock_start_vz')
    for i in range(4): # 4 works but 3 doesn't
        px,py,pz = positions_list[i]
        vx,vy,vz = velocities_list[i]
        equations.extend([Eq(( rock_start_vy - vy ) * ( rock_start_x - px ), ( rock_start_vx - vx ) * ( rock_start_y - py )), Eq(( rock_start_vz - vz ) * ( rock_start_y - py ),  ( rock_start_vy - vy) * ( rock_start_z - pz )) ])
    for equation in equations:
        print(equation)
    solution = solve(equations,(rock_start_x,rock_start_y,rock_start_z,rock_start_vx,rock_start_vy,rock_start_vz))
    print(solution)
    rock_start_x, rock_start_y, rock_start_z = solution[0][0],solution[0][1],solution[0][2]
    start_pos_multiple = rock_start_x + rock_start_y + rock_start_z
    return start_pos_multiple
total = count_intersections(positions_list,velocities_list)


print('total:',total)
test_dictionary = {
    '2023_Day24_input':
    {'attempts':(None),
    'low':None,'high':None,'answer':566373506408017},
    '2023_Day24_testinput':
    {'answer':47},
}

from testmodule import test_function
test_function(test_dictionary,filename,total)
'''


'''