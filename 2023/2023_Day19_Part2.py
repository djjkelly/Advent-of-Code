#!/usr/bin/env python3
#https://adventofcode.com/2023/day/19

import copy

with open("2023/2023_Day19_testinput.txt",'r') as file_object:
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

paths_to_explore = [{'path':['in'],'x': {'min':1,'max':4000}, 'm': {'min':1,'max':4000}, 'a': {'min':1,'max':4000}, 's': {'min':1,'max':4000}}]
accepted_paths = []
while paths_to_explore != []:
    current_path = paths_to_explore[0]
    paths_to_explore.pop(0)
    current_workflow = workflows[current_path['path'][-1]]
    print('current_path with ranges:',current_path)
    for rule in current_workflow:
        if ':' in rule:
            new_path = copy.deepcopy(current_path) # each rule splits the path in two (current_path and new_path)
            action = rule.split(':')[1]
            rule = rule.split(':')[0]
            category_to_consider = rule[0]
            conditional = rule[1]
            check_number = int(rule[2:])
            print('category_to_consider:',category_to_consider,'conditional:',conditional,'number_to_check:',check_number, 'action:', action)
            if current_path[category_to_consider]['min'] < check_number < current_path[category_to_consider]['max']: # not sure this condition will ever be not met.
                if conditional == '<':
                    current_path[category_to_consider]['min'] = check_number # doesn't meet the condition, so continues to next rule
                    new_path[category_to_consider]['max'] = check_number # meets the condition, so either ends or moves to a new workflow
                    if action == 'A':
                        accepted_paths.append(new_path)
                        continue
                    elif action != 'R':
                        if action == 'x>2440':
                            print('x2440 error found!')
                        new_path['path'].append(action)
                        paths_to_explore.append(new_path)
                        continue
                elif conditional == '>':
                    current_path[category_to_consider]['max'] = check_number # doesn't meet the condition, so continues to next rule
                    new_path[category_to_consider]['min'] = check_number # meets the condition, so either ends or moves to a new workflow
                    if action == 'A':
                        accepted_paths.append(new_path)
                        continue
                    elif action != 'R':
                        if action == 'x>2440':
                            print('x2440 error found!')
                        new_path['path'].append(action)
                        paths_to_explore.append(new_path)
                        continue
        else:
            action = rule
            if action == 'A':
                accepted_paths.append(current_path)
            elif action != 'R':
                if action == 'x>2440':
                    print('x2440 error found!')
                current_path['path'].append(action)
                paths_to_explore.append(current_path)
            
total = 0
for part in accepted_paths:
    print()
    line_total = 1
    for value in part.values():
        print(value)
        if 'min' in value:
            line_total *= int(value['max']) - int(value['min'])
            total += line_total
print('total',total)

'''
Part2 testinput should give an answer of 167409079868000:

For Part2 we need to look at the total number of combinations of "category" values which can be accepted.
One approach might be to go through the normal network as above but scope out each path individually.
At each conditional, we branch the path off into two directions.
For each path you would have a minimum and maximum acceptable value (a range).
If we hit an R that path dies.
If we hit an A, then the number of combinations represented by our ranges gets added to the number of acceptable combinations.
Once added, the A path can be removed from the paths_to_explore.
The number of combinations represented can be expressed as a multiple (max1-min1 * max2-min2 * max3-min3 * max4-min4)

I want to structure this as something like a dict of dicts:
{'x': {'min':'1','max':'4000'}, 'm': {'min':'1','max':'4000'}, 'a': {'min':'1','max':'4000'}, 's': {'min':'1','max':'4000'}}
Every time the path splits, one path is explored an another is stored for later.

Maybe another level of abstraction can be added:
[{'path': ['in']}:{'x': {'min':'1','max':'4000'}, 'm': {'min':'1','max':'4000'}, 'a': {'min':'1','max':'4000'}, 's': {'min':'1','max':'4000'}}]

The new_path and the current_path will differ by at most one category.
The current_path and new_path should both be overwritten when the variable is reused.

Testinput is pretty close. 167486317990679 instead of 167409079868000.
There seems to be a problem that the split ranges overlap by 1.
'''