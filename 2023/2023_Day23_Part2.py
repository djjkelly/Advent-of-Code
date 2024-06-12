#!/usr/bin/env python3
#https://adventofcode.com/2023/day/23

folder = '2023/'
filename = '2023_Day23_input'
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
                (fdv,fdh) = directions[new_direction]
                if new_direction == new_character:
                    end_state = (new_v + fdv, new_h + fdh, new_direction)
                else:
                    end_state = (new_v + fdv, new_h + fdh, new_character)
                return end_state, section_length
(restricted_v,restricted_h,initial_end_direction),_ = explore_section((0,1,'v'))
restricted_direction = opposite_directions[initial_end_direction]
restricted_state = restricted_v,restricted_h,restricted_direction

def explore_all_sections(input_list,initial_state):
    queue = [initial_state]
    seen = []
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
            start_end_mapping[(end_v,end_h,opposite_of_end_direction)] = (start_v,start_h,opposite_of_start_direction) # found a mistake here

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
            if new_character in directions:
                new_state = (end_v,end_h,new_direction)
                if new_state not in queue and new_state not in seen and new_state != restricted_state:# restricted_state stops the first section being explored backwards
                    queue.append(new_state)
                    seen.append(new_state) # to prevent infinite loops when sections have already been visited
    return section_lengths, start_end_mapping
initial_state = (initial_v,initial_h,initial_direction)
section_lengths, start_end_mapping = explore_all_sections(input_list,initial_state)
for start,end in start_end_mapping.items():
    if end in section_lengths:
        print('start:',start,'. end:',end,'. section length:',section_lengths[end])
    else:
        print('start:',start,'. end:',end,'. section length not found')

'''
Now that we can travel in any direction along a section, I need to record whether the path has already been taken.
It should be sufficient to do this using a start and end coordinate for each section.

To decide whether a path should be added to the queue, any 'directions' character should be permissible.

In order to not step on any tile twice, we just need to avoid revisiting all endpoints of the sections.
'''

def find_longest_path_length(section_lengths, start_end_mapping, initial_state):
    first_section_end_state = start_end_mapping[initial_state]
    running_total = section_lengths[first_section_end_state]
    coordinates_explored = [(first_section_end_state[0],first_section_end_state[1])]
    paths_to_explore = [(first_section_end_state, running_total, coordinates_explored)]
    max_total = 0
    while paths_to_explore:
        current_path = paths_to_explore.pop(0)
        end_v, end_h, end_direction = current_path[0]
        current_total = current_path[1]
        if end_v is not None and end_h is not None:
            for new_direction in directions:
                coordinates_explored = current_path[2][:] # using slicing to create a copy of the list
                next_start_state = (end_v, end_h, new_direction)
                if next_start_state in start_end_mapping:
                    next_end_state = start_end_mapping[next_start_state]
                    next_coordinates = (next_end_state[0],next_end_state[1])
                    if next_coordinates not in coordinates_explored:
                        coordinates_explored.append(next_coordinates)
                        paths_to_explore.append((next_end_state,current_total + section_lengths[next_end_state],coordinates_explored))
        else:
            total = current_total
            if total > max_total:
                max_total = total
            print('total:',total,'. max_total:',max_total)
    return max_total
total = find_longest_path_length(section_lengths, start_end_mapping,initial_state)

print('total:',total)
test_dictionary = {
    '2023_Day23_input':
    {'attempts':(3300,3600),
    'low':3600,'high':None,'answer':None},
    '2023_Day23_testinput':
    {'answer':154},
}

from testmodule import test_function
test_function(test_dictionary,filename,total)
'''
The longest path in the testinput goes:
(5,3) 'v'
(13,5) 'v'
(19,13) '>'
(13,13) '^' - this is missing from the section_lengths
(3,11) '^'
(11,21) 'v'
(19,19) 'v'
(None,None)

highest value achieved so far:
3614

'''