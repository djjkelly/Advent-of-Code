#!/usr/bin/env python3
#https://adventofcode.com/2023/day/23

folder = '2023/'
filename = '2023_Day23_testinput'
extension = '.txt'
full_path = folder + filename + extension
with open(full_path,'r') as file_object:
    file_content = file_object.readlines()
total = 0
input_list = []
for line in file_content:
    line = line.strip()
    input_list.append(line)
vertical_length = len(input_list)
horizontal_length = len(input_list[0])
start_v = 0
start_h = 1
end_v = vertical_length - 1
end_h = horizontal_length - 2
start_direction = 'down'
# these simplifications are true for both test and real input.

directions = {
    'down':(1,0),
    'right':(0,1),
    'up':(-1,0),
    'left':(0,-1)
}
forced_directions = {
    'v':'down',
    '>':'right',
    '^':'up',
    '<':'left',
}

def is_in_bounds(new_v,new_h):
    return 1 <= new_v < vertical_length - 1 and 1 <= new_h < horizontal_length - 1 # we never have to explore the outer edge.

'''
Any section of path which does not contain a fork can have its length stored in memory for later reuse.
If the start and end coordinates and direction are recorded, this memoised path can be accessed from both sides.

It looks like there aren't any > symbols going straight into the forest.
Also, single sections don't seem to have 
Rather the slippery slopes seem to act as 'gates' at both ends of each section.
It looks like, if I can't get in one end, then I can't get out the other either.
If I can get in one end of the section, then I can get out the other.
The sections basically all start/end with a '<', '>', 'v', '^' symbol.
This also means that all "sections" are one-way.
'''

def explore_section(start_state):
    v,h,direction = start_state
    section_length = 0
    section_evaluation_ongoing = True
    while section_evaluation_ongoing:
        section_length += 1
        for new_direction,(dv,dh) in directions.items():
            if (v,h) == (vertical_length - 2,horizontal_length - 2): # end of puzzle (one move away from end)
                section_length += 1
                section_evaluation_ongoing = False
                print('reached end of puzzle!')
                new_v,new_h = None,None
                break
            if (-dv,-dh) == directions[direction]:
                continue # can't go back on ourselves
            new_v, new_h = v + dv, h + dh
            if not is_in_bounds(new_v,new_h):
                continue # can't go out of bounds
            new_character = input_list[new_v][new_h]
            if new_character == '#': # ignore forest
                continue
            if new_character in forced_directions: # has reached the end of the section!
                section_evaluation_ongoing = False
                section_length += 1
                v,h,direction = new_v,new_h,new_direction
                break
            if new_character == '.':
                v,h,direction = new_v,new_h,new_direction
                break


    end_state = (new_v,new_h,new_direction)
    return end_state, section_length
#end_state, section_length = explore_section((0,1,'down')) # aiming for 18,19
#print('end_state',end_state,'section_length',section_length)

def explore_all_sections(input_list):
    initial_state = (start_v,start_h,start_direction)
    queue = [initial_state]
    explored_sections = {}
    while queue:
        start_state = queue.pop(0)
        end_state,section_length = explore_section(start_state)
        if end_state in explored_sections:
            print('end state dupicate encountered - check this!')
        else:
            explored_sections[end_state] = section_length
        end_v,end_h,end_direction = end_state[0],end_state[1],end_state[2]
        if end_v == None or end_h == None:
            continue
        end_dv,end_dh = directions[end_direction]
        v,h = end_v + end_dv, end_h + end_dh
        print(f'section ends at ({end_v},{end_h}), new state at ({v},{h})')
        # find all viable directions for the next sections to be added to the queue
        for new_direction, (dv,dh) in directions.items():
            if (dv,dh) == (-end_dv,-end_dh):
                continue
            new_v, new_h = v + dv,h + dh
            if not is_in_bounds (new_v,new_h):
                continue
            new_character = input_list[new_v][new_h]
            if new_character == '#':
                continue
            if new_character in forced_directions:
                if forced_directions[new_character] == new_direction:
                    print('new section found! adding to queue')
                    new_state = (new_v,new_h,new_direction)
                    if new_state not in queue:
                        queue.append(new_state)
    return explored_sections
explored_sections = explore_all_sections(input_list)
# seems ok so far. For testinput it identifies 12 sections and the new states seem to be at the correct points


print('total:',total)
test_dictionary = {
    '2023_Day23_input':
    {'attempts':(None),
    'low':None,'high':None,'answer':None},
    '2023_Day23_testinput':
    {'answer':94},
}

from testmodule import test_function
test_function(test_dictionary,filename,total)
'''

'''