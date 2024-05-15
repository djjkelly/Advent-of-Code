#!/usr/bin/env python3
#https://adventofcode.com/2023/day/19

import copy

with open("2023/2023_Day19_input.txt",'r') as file_object:
    file_content = file_object.readlines()
    before_line_break = True
    workflows = {}
    for line in file_content:
        if line == '\n':
            before_line_break = False
            continue
        line = line.strip()
        if before_line_break:
            workflow_name = line.split('{')[0]
            rules = line.split('}')[0].split('{')[1].split(',')
            workflows[workflow_name] = rules

paths_to_explore = [{'path': ['in'], 'x': {'min': 1, 'max': 4000}, 'm': {'min': 1, 'max': 4000}, 'a': {'min': 1, 'max': 4000}, 's': {'min': 1, 'max': 4000}}]
accepted_paths = []

while paths_to_explore:
    current_path = paths_to_explore.pop(0)
    current_workflow = workflows[current_path['path'][-1]]
    for rule in current_workflow:
        if ':' in rule:
            new_path = copy.deepcopy(current_path)  # each rule splits the path in two (current_path and new_path)
            action = rule.split(':')[1]
            condition = rule.split(':')[0]
            category_to_consider = condition[0]
            conditional = condition[1]
            check_number = int(condition[2:])
            
            if conditional == '<':
                new_path[category_to_consider]['max'] = check_number - 1  # meets the condition, so either ends or moves to a new workflow
                current_path[category_to_consider]['min'] = check_number  # doesn't meet the condition, so continues to next rule
                if action == 'A':
                    accepted_paths.append(new_path)
                elif action != 'R':
                    new_path['path'].append(action)
                    paths_to_explore.append(new_path)
            
            elif conditional == '>':
                new_path[category_to_consider]['min'] = check_number + 1  # meets the condition, so either ends or moves to a new workflow
                current_path[category_to_consider]['max'] = check_number  # doesn't meet the condition, so continues to next rule
                if action == 'A':
                    accepted_paths.append(new_path)
                elif action != 'R':
                    new_path['path'].append(action)
                    paths_to_explore.append(new_path)
        else:
            action = rule
            if action == 'A':
                accepted_paths.append(current_path)
            elif action != 'R':
                current_path['path'].append(action)
                paths_to_explore.append(current_path)

# Calculate the total number of accepted combinations
total = 0
for path in accepted_paths:
    #print('path:',path)
    line_total = 1
    for key, value in path.items():
        if 'min' in value:
            line_total *= (int(value['max']) - int(value['min']) + 1)  # +1 to count first as well as last possibility
    total += line_total

print('\ntotal: ', total)

'''
125744206494820 is the correct answer!
Part2 testinput should give an answer of 167409079868000

For Part2 we need to look at the total number of combinations of "category" values which can be accepted.
At each conditional, we branch the path off into two directions.
For each path you would have a minimum and maximum acceptable value (a range).
If we hit an R that path dies (doesn't get appended).
If we hit an A, then the number of combinations represented by our ranges gets added to the number of acceptable combinations.
Once added, the A path can be removed from the paths_to_explore.
The number of combinations represented can be expressed as a multiple (max1-min1+1) * (max2-min2+1) * (max3-min3+1) * (max4-min4+1)

The new_path and the current_path will differ by at most one category.
The current_path and new_path should both be overwritten when the variable is reused.

It seems that the testinput and real input have been generated such that the check_number never falls outside the range.

'''