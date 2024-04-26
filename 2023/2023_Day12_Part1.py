#!/usr/bin/env python3
#https://adventofcode.com/2023/day/12

import math
from itertools import product

with open("2023/2023_Day12_testinput.txt") as file_object:
    file_content = file_object.readlines()

content_list = []
for line in file_content:
    line = line.strip()
    condition_records = line.split()[0]
    damaged_group_sizes = line.split()[1]
    damaged_group_sizes = damaged_group_sizes.split(',')
    content_list.append([condition_records,damaged_group_sizes])

def generate_combinations(uncertain_springs):
    all_combinations = [''.join(seq) for seq in product('01',repeat=uncertain_springs)]
    return all_combinations

def remove_wrong_numbers(test_list,number_expected):
    new_test_list = test_list.copy()
    for string in test_list:
        count = string.count('1')
        if count != number_expected:
            new_test_list.remove(string)
    return new_test_list

def make_full_strings(condition_records,test_list):
    print('Condition records: ',condition_records)
    new_list = []
    for test_string in test_list:
        test_index = 0
        new_condition_records = condition_records
        for condition_index,character in enumerate(condition_records):
            if character == '?':
                new_condition_records = new_condition_records[:condition_index]+test_string[test_index] + new_condition_records[condition_index + 1:]
                #print(f'replacing character at {condition_index} with new character: {test_string[test_index]}')
                test_index += 1
        new_list.append(new_condition_records)
    return new_list

def check_permutation(string):
    is_viable = False
    return is_viable

'''
Test input expectations:
Number of arrangements per line should be 1, 4, 1, 1, 4, 10
Total for all lines should be 21 arrangements (1 + 4 + 1 + 1 + 4 + 10)
'''
total_possibilities = 0
for line_no,line in enumerate(content_list):
    print(f'\nStarting line {line_no}: {line}')
    condition_records, damaged_group_sizes = line[0],line[1]
    line_possibilities = 0
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
        else:
            print(f'Error - unexpected character encountered. Line {line_no} at character number {char_no}: \'{character}\'')
    total_springs = char_no + 1
    #print(f'total of {total_springs} springs. uncertain_springs: {uncertain_springs}.')
    for group in damaged_group_sizes:
        damaged_springs_total += int(group)
    springs_to_find = damaged_springs_total - damaged_springs_found
    #print(f'{damaged_springs_found} springs found out of a total of {damaged_springs_total} damaged springs. Remaining springs_to_find: {springs_to_find}')
    print(f'looking for springs_to_find of {springs_to_find} amongst {uncertain_springs} uncertain_springs')
    test_list = generate_combinations(uncertain_springs)
    test_list = remove_wrong_numbers(test_list,springs_to_find)
    #print('test list with wrong combinations removed:',test_list)
    #print('combinations predicted:',math.comb(uncertain_springs,springs_to_find))
    test_list = make_full_strings(condition_records,test_list)
    print('full strings test list: ',test_list)


print('\nTotal possibilities: ',total_possibilities)
'''
I need to exclude damaged groups which are directly next to each other.

'''