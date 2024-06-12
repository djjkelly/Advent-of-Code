#!/usr/bin/env python3
#https://adventofcode.com/2023/day/23

folder = '2023/'
filename = '2023_Day23_testinput'
extension = '.txt'
full_path = folder + filename + extension
with open(full_path,'r') as file_object:
    file_content = file_object.readlines()
input_list = []
for line in file_content:
    line = line.strip()
    input_list.append(line)
vertical_length = len(input_list)
horizontal_length = len(input_list[0])
initial_v = 0
initial_h = 1
end_v = vertical_length - 2
end_h = horizontal_length - 2
initial_direction = 'v'
# these simplifications are true for both test and real input.

directions = {
    'v':(1,0),
    '>':(0,1),
    '^':(-1,0),
    '<':(0,-1)
}

opposite_directions = {
    'v':'^',
    '>':'<',
    '^':'v',
    '<':'>',
    None:None
}

def is_in_bounds(new_v,new_h):
    return 0 <= new_v < vertical_length - 1 and 0 <= new_h < horizontal_length - 1

def explore_section(start_state):
    v,h,direction = start_state
    dv, dh = directions[direction]
    section_length = 1
    v,h = v + dv, h + dh
    while True: # each iteration represents a step along the path section
        section_length += 1
        for new_direction,(dv,dh) in directions.items():
            if (v,h) == (end_v,end_h): # end of puzzle (one move away from end)
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

def explore_all_sections(input_list,initial_state):
    queue = [initial_state]
    section_lengths = {}
    start_end_mapping = {}
    while queue:
        start_state = queue.pop(0)
        end_state,section_length = explore_section(start_state)
        end_v,end_h,end_direction = end_state[0],end_state[1],end_state[2]
        if end_state not in section_lengths:
            section_lengths[end_state] = section_length
            start_end_mapping[start_state] = end_state

            # now adding the opposite direction for the same path!
            opposite_of_end_direction = opposite_directions[end_direction]
            start_v, start_h, start_direction = start_state
            opposite_of_start_direction = opposite_directions[start_direction]
            section_lengths[(start_v,start_h,opposite_of_start_direction)] = section_length
            start_end_mapping[(end_v,end_h,opposite_of_end_direction)] = (end_v,end_h,opposite_of_end_direction)

        if end_v == None or end_h == None:
            continue
        dv,dh = directions[end_direction]
        # find all viable directions for the next sections to be added to the queue
        for new_direction,(new_dv,new_dh) in directions.items():
            if (new_dv,new_dh) == (-dv,-dh):
                continue
            new_v , new_h = (end_v + new_dv) , (end_h + new_dh)
            if not is_in_bounds (new_v,new_h):
                continue
            new_character = input_list[new_v][new_h]
            if new_character == '#':
                continue
            if new_character in directions: # changed this to explore all unexplored directions
                new_state = (end_v,end_h,new_direction) # changed new_character to new_direction - no longer following character directions
                if new_state not in queue:
                    queue.append(new_state)
    return section_lengths, start_end_mapping
initial_state = (initial_v,initial_h,initial_direction)
section_lengths, start_end_mapping = explore_all_sections(input_list,initial_state)
for section,length in section_lengths.items():
    print('section end: ',section,'length',length) # central lengths seem off by one?

'''
Now that we can travel in any direction along a section, I need to record whether the path has already been taken.
It should be sufficient to do this using a start and end coordinate for each section.

To decide whether a path should be added to the queue, any 'directions' character should be permissible.
'''

def find_longest_path_length(section_lengths, start_end_mapping, initial_state):
    first_section_end_state = start_end_mapping[initial_state]
    running_total = section_lengths[first_section_end_state]
    states_explored = set((initial_state,))
    paths_to_explore = [(first_section_end_state, running_total, states_explored)]
    list_of_totals = []
    while paths_to_explore:
        current_path = paths_to_explore.pop(0)
        v, h, direction = current_path[0]
        current_total = current_path[1]
        states_explored = current_path[2]
        opposite_direction = opposite_directions[direction]
        states_explored.add((v,h,opposite_direction))
        if v is not None and h is not None:
            directions_checked_count = 0
            for new_direction,(ndv,ndh) in directions.items():
                directions_checked_count += 1
                if directions_checked_count == 5:
                    break
                dv,dh = directions[direction]
                if (dv,dh) == (-ndv,-ndh):
                    'continue'
                next_start_state = (v, h, new_direction)
                if next_start_state in start_end_mapping and next_start_state not in states_explored: # changed to depend on states_explored
                    next_end_state = start_end_mapping[next_start_state]
                    states_explored.add(next_start_state)
                    paths_to_explore.append((next_end_state,current_total + section_lengths[next_end_state],states_explored))
        else:
            total = current_total # + section_lengths[(None,None,None)] this was double_counting the end section!
            list_of_totals.append(total)
    print(f'list_of_totals {list_of_totals}')
    max_total = 0
    for total in list_of_totals:
        if total > max_total:
            max_total = total
    return max_total
total = find_longest_path_length(section_lengths, start_end_mapping,initial_state)

print('total:',total)
test_dictionary = {
    '2023_Day23_input':
    {'attempts':(None),
    'low':None,'high':None,'answer':None},
    '2023_Day23_testinput':
    {'answer':154},
}

from testmodule import test_function
test_function(test_dictionary,filename,total)
'''


'''