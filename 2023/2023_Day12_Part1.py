#!/usr/bin/env python3
#https://adventofcode.com/2023/day/12

with open("2023/2023_Day12_testinput.txt") as file_object:
    file_content = file_object.readlines()

def count_possibilities(condition_records,damaged_group_sizes):
    global call_depth
    call_depth += 1
    current_character = condition_records[0]
    current_group = damaged_group_sizes[0]
    # base case - no more condition records
    if condition_records == '':
        if damaged_group_sizes == ():
            call_depth -= 1
            return 1
        else:
            call_depth -= 1
            return 0
    # base case - not enough damaged group sizes
    if damaged_group_sizes == ():
        if '#' in condition_records:
            call_depth -= 1
            return 0 # remaining damaged parts cannot be accounted for in damaged_group_sizes
        else:
            call_depth -= 1
            return 1 # damaged groups and # characters exhausted - found a possibility
    result = 0
    if condition_records[0] == '.' or condition_records[0] == '?': # this branch assumes '?' is a '.'... these branches will explore first
        result += count_possibilities(condition_records[1:],damaged_group_sizes) # damaged group sizes remain unchanged - no damaged springs assigned

    # this branch assumes '?' is a '#'
    if condition_records[0] == '#' or condition_records[0] == '?':
        if damaged_group_sizes[0] <= len(condition_records): # no point evaluating if there aren't enough characters left
            if '.' not in condition_records[:damaged_group_sizes[0]]: # looks along the length of the group size to check that all could be damaged.
                if damaged_group_sizes[0] == len(condition_records):
                    result += count_possibilities(condition_records[1:],damaged_group_sizes[1:])
                elif condition_records[damaged_group_sizes[0] + 1] == '.':
                    result += count_possibilities(condition_records[1:],damaged_group_sizes[1:])
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
    print(condition_records)
    print(damaged_group_sizes)
    line_total = count_possibilities(condition_records,damaged_group_sizes)
    print('line total:',line_total)
    total += line_total
print('total:',total)


'''
Correct answer for Part 1 - 7260

'''