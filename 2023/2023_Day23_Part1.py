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
end_v = vertical_length - 2
end_h = horizontal_length - 2
start_direction = 'v'
# these simplifications are true for both test and real input.

directions = {
    'v':(1,0),
    '>':(0,1),
    '^':(-1,0),
    '<':(0,-1)
}

def is_in_bounds(new_v,new_h):
    return 0 <= new_v < vertical_length - 1 and 0 <= new_h < horizontal_length - 1

'''
Any section of path which does not contain a fork can have its length stored in memory for later reuse.
If the start and end coordinates and direction are recorded, this memoised path can be accessed from both sides.

It looks like there aren't any '>' symbols going straight into the forest.
Also, single sections don't seem to have any '<', '>', 'v', '^' symbols on them.
Rather the slippery slopes seem to act as 'gates' at both ends of each section.
It looks like, if I can't get in one end, then I can't get out the other either.
If I can get in one end of the section, then I can also get out the other.
The sections all start/end with a '<', '>', 'v', '^' symbol (except first and last).
This also means that all "sections" are one-way.
'''

def explore_section(start_state):
    v,h,direction = start_state
    section_length = 0
    while True: # each iteration represents a step along the path section
        section_length += 1
        for new_direction,(dv,dh) in directions.items():
            if (v,h) == (end_v,end_h): # end of puzzle (one move away from end)
                section_length += 1
                print('reached end of puzzle!')
                end_state = (None,None,None)
                return end_state, section_length
            if (-dv,-dh) == directions[direction]:
                continue # can't go back on ourselves
            new_v, new_h = v + dv, h + dh
            if not is_in_bounds(new_v,new_h):
                continue # can't go out of bounds
            new_character = input_list[new_v][new_h]
            if new_character == '#': # ignore forest
                continue
            if new_character == '.':
                v,h,direction = new_v,new_h,new_direction
                break
            if new_character in directions: # has reached the end of the section!
                section_length += 1
                (fdv,fdh) = directions[new_character]
                end_state = (new_v + fdv, new_h + fdh,new_character)
                return end_state, section_length
#end_state, section_length = explore_section((0,1,'down')) # aiming for 18,19
#print('end_state',end_state,'section_length',section_length)

def explore_all_sections(input_list):
    initial_state = (start_v,start_h,start_direction)
    queue = [initial_state]
    section_lengths = {}
    start_end_mapping = {}
    while queue:
        start_state = queue.pop(0)
        end_state,section_length = explore_section(start_state)
        if end_state in section_lengths:
            print('end state dupicate encountered - check this!')
        else:
            section_lengths[end_state] = section_length
            start_end_mapping[start_state] = end_state
        end_v,end_h,end_direction = end_state[0],end_state[1],end_state[2]
        if end_v == None or end_h == None:
            continue
        end_dv,end_dh = directions[end_direction]
        v,h = end_v, end_h
        print(f'section ends at ({end_v},{end_h}), new state at ({v},{h})')
        # find all viable directions for the next sections to be added to the queue
        for (dv,dh) in directions.values():
            if (dv,dh) == (-end_dv,-end_dh):
                continue
            new_v, new_h = v + dv,h + dh
            if not is_in_bounds (new_v,new_h):
                continue
            new_character = input_list[new_v][new_h]
            if new_character == '#':
                continue
            if new_character in directions:
                new_state = (new_v,new_h,new_character)
                if new_state not in queue:
                    queue.append(new_state)
    return section_lengths, start_end_mapping

section_lengths, start_end_mapping = explore_all_sections(input_list)
# seems ok so far. For testinput it identifies 12 sections and the new states seem to be at the correct points
for section,length in section_lengths.items():
    print('section end: ',section,'length',length) # central lengths seem off by one?

def find_longest_path_length(section_lengths, start_end_mapping):
    first_section_end_state = start_end_mapping[(start_v,start_h,start_direction)]
    running_total = section_lengths[first_section_end_state]
    paths_to_explore = [(first_section_end_state,running_total)]
    list_of_totals = []
    while paths_to_explore:
        current_path = paths_to_explore.pop(0)
        v, h, direction = current_path[0]
        current_total = current_path[1]
        if v is not None and h is not None:
            (dv,dh) = directions[direction]
            for new_direction,(ndv,ndh) in directions.items():
                if (dv,dh) == (-ndv,-ndh):
                    'continue'
                next_status = (v + ndv, h + ndh, new_direction)
                if next_status in start_end_mapping:
                    next_end_status = start_end_mapping[next_status]
                    paths_to_explore.append((next_end_status,current_total + section_lengths[next_end_status]))
        else:
            total = current_total + section_lengths[(None,None,None)]
            list_of_totals.append(total)
    print(f'list_of_totals {list_of_totals} - should be ( 90, 82,  74, 82, 86, 94 )')
    max_total = 0
    for total in list_of_totals:
        if total > max_total:
            max_total = total
    return max_total
total = find_longest_path_length(section_lengths, start_end_mapping)

print('total:',total)
test_dictionary = {
    '2023_Day23_input':
    {'attempts':(None),
    'low':None,'high':2118,'answer':None},
    '2023_Day23_testinput':
    {'answer':94},
}

from testmodule import test_function
test_function(test_dictionary,filename,total)
'''
2118 - answer too high
testinput totals are incorrect by either 1 or 2 (too high)

'''