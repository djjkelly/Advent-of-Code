#!/usr/bin/env python3
#https://adventofcode.com/2023/day/12

folder = '2023/'
filename = '2023_Day12_input'
extension = '.txt'
full_path = folder + filename + extension

with open(full_path) as file_object:
    file_content = file_object.readlines()

def count_possibilities(string,tuple):
    global call_depth
    call_depth += 1
    # base case - no more condition records
    if string == '':
        if tuple == ():
            call_depth -= 1
            return 1
        else:
            call_depth -= 1
            return 0
    # base case - not enough damaged group sizes
    if tuple == ():
        if '#' in string:
            call_depth -= 1
            return 0 # remaining damaged parts cannot be accounted for in damaged_group_sizes
        else:
            call_depth -= 1
            return 1 # damaged groups and # characters exhausted - found a possibility
    result = 0
    current_character = string[0]
    current_group = tuple[0]
    # this branch assumes '?' is a '.'... these branches will explore first
    if current_character == '.' or current_character == '?':
        result += count_possibilities(string[1:],tuple) # damaged group sizes remain unchanged - no damaged springs assigned

    # this branch assumes '?' is a '#'
    if current_character == '#' or current_character == '?':
        if tuple[0] <= len(string): # no point evaluating if there aren't enough characters left
            if '.' not in string[:current_group]: # looks along the length of the group size to check that all could be damaged.
                if tuple[0] == len(string): # group ends at end of string
                    result += count_possibilities(string[current_group:],tuple[1:])
                elif string[current_group] == '.' or string[current_group] == '?': # group ends when interrupted by a '.'
                    result += count_possibilities(string[current_group+1:],tuple[1:]) # the next char '.' or '?' should be skipped ('?' treated as '.') 
    call_depth -= 1
    return result

total = 0
for line in file_content:
    call_depth = 0
    line = line.strip()
    condition_records = line.split()[0]
    damaged_group_sizes = []
    for group in line.split()[1].split(','):
        damaged_group_sizes.append(int(group))
    damaged_group_sizes = tuple(damaged_group_sizes)
    #print(condition_records)
    #print(damaged_group_sizes)
    line_total = count_possibilities(condition_records,damaged_group_sizes)
    print('line total:',line_total)
    total += line_total
print('total:',total)


'''
Correct answer for Part 1 - 7260

'''
test_dictionary = {
    '2023_Day12_input':
    {'answer':7260},
}

from testmodule import test_function
test_function(test_dictionary,filename,total)