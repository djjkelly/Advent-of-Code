#!/usr/bin/env python3
#https://adventofcode.com/2023/day/12

import math
from itertools import product
import cProfile

with open("2023/2023_Day12_testinput.txt") as file_object:
    file_content = file_object.readlines()

content_list = []
for line in file_content:
    line = line.strip()
    condition_records = line.split()[0]
    damaged_group_sizes = line.split()[1]
    damaged_group_sizes = damaged_group_sizes.split(',')
    expansion_factor = 1  #EXPANSION FACTOR
    expanded_condition_records = condition_records
    expanded_damaged_group_sizes = damaged_group_sizes * expansion_factor
    for i in range(expansion_factor - 1):
        expanded_condition_records += '?'
        expanded_condition_records += condition_records
    content_list.append([expanded_condition_records,expanded_damaged_group_sizes])

def generate_combinations(uncertain_springs,number_expected):
    relevant_combinations = []
    for seq in product('01',repeat=uncertain_springs):
        if seq.count('1') == number_expected:
            relevant_combinations.append(''.join(seq))
    return relevant_combinations

def make_full_strings(condition_records,test_list):
    new_list = []
    for test_string in test_list:
        test_index = 0
        new_condition_records = condition_records
        for condition_index,character in enumerate(condition_records):
            if character == '?':
                new_condition_records = new_condition_records[:condition_index]+test_string[test_index] + new_condition_records[condition_index + 1:]
                test_index += 1
        new_list.append(new_condition_records)
    return new_list

def count_possibilities(input_list,damaged_group_sizes):
    count = 0
    for string in input_list:
        group_sizes = []
        group_size = 0
        for character in string:
            if character == '#' or character == '1':
                group_size += 1
            if character == '.' or character == '0':
                if group_size > 0:
                    group_sizes.append(str(group_size))
                group_size = 0
        if group_size > 0:
            group_sizes.append(str(group_size))
        if group_sizes == damaged_group_sizes:
            count += 1
    return count

'''
Test input expectations:
Number of arrangements per line should be 1, 16384, 1, 16, 2500, 506250
Total for all lines should be 525152 arrangements (1 + 16384 + 1 + 16 + 2500 + 506250)
'''

def calculate(condition_records,damaged_group_sizes):
    operational_springs = 0
    uncertain_springs = 0
    damaged_springs_found = 0
    damaged_springs_total = 0
    for char_no,character in enumerate(condition_records):
        if character == '?':
            uncertain_springs += 1
        elif character == '.':
            operational_springs += 1
        elif character == '#':
            damaged_springs_found += 1
    total_springs = char_no + 1
    for group in damaged_group_sizes:
        damaged_springs_total += int(group)
    damaged_springs_to_find = damaged_springs_total - damaged_springs_found
    print(f'looking for damaged_springs_to_find of {damaged_springs_to_find} out of {uncertain_springs} uncertain_springs')
    test_list = generate_combinations(uncertain_springs,damaged_springs_to_find)
    test_list = make_full_strings(condition_records,test_list)
    line_possibilities = count_possibilities(test_list,damaged_group_sizes)
    #print('line_possibilities: ',line_possibilities)
    return line_possibilities

total_possibilities = 0
for line_no,line in enumerate(content_list):
    #line = content_list[848]
    print(f'\nStarting line {line_no+1}: {line}')
    condition_records, damaged_group_sizes = line[0],line[1]
    operational_springs = 0
    uncertain_springs = 0
    damaged_springs_found = 0
    damaged_springs_total = 0
    for char_no,character in enumerate(condition_records):
        if character == '?':
            uncertain_springs += 1
        elif character == '.':
            operational_springs += 1
        elif character == '#':
            damaged_springs_found += 1
    total_springs = char_no + 1
    for group in damaged_group_sizes:
        damaged_springs_total += int(group)
    damaged_springs_to_find = damaged_springs_total - damaged_springs_found
    print(f'looking for damaged_springs_to_find of {damaged_springs_to_find} out of {uncertain_springs} uncertain_springs')
    #cProfile.run('generate_combinations(uncertain_springs,damaged_springs_to_find)')
    test_list = generate_combinations(uncertain_springs,damaged_springs_to_find)
    #print('combinations predicted:',math.comb(uncertain_springs,damaged_springs_to_find))
    test_list = make_full_strings(condition_records,test_list)
    line_possibilities = count_possibilities(test_list,damaged_group_sizes)
    print('line_possibilities: ',line_possibilities)
    total_possibilities += line_possibilities

print('\nTotal possibilities: ',total_possibilities)
'''
I would guess that given the pattern repeats, it should be possible to use the repeating pattern as the basis.

In general if we had 5 repeating units we would need the original number of combinations^5.

I've not figured out how to account for the 4 extra ? symbols inserted in the line.
Maybe one option is to assume that all 5 repeating units had the '?', then adjust the line_possibilities downwards - not sure how to adjust.
Alternatively it might be better to assume that it's not there and then adjust the line_possibilities upwards.

'''