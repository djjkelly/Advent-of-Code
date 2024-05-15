#!/usr/bin/env python3
#https://adventofcode.com/2023/day/19

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

def process_action(action):
    print(f'processing action {action}...')
    part_accepted = None
    next_workflow = None
    if action == 'R':
        part_accepted = False
    elif action == 'A':
        part_accepted = True
    else:
        next_workflow = action
    return part_accepted,next_workflow

paths_to_explore = [{'path':['in'],'x': {'min':1,'max':4000}, 'm': {'min':1,'max':4000}, 'a': {'min':1,'max':4000}, 's': {'min':1,'max':4000}}]
accepted_paths = []
while paths_to_explore != []:
    current_path = paths_to_explore[0]
    paths_to_explore.pop(0)
    current_workflow = workflows[current_path['path'][-1]]
    print('current_path with ranges:',current_path)
    for rule in current_workflow: # each rule splits the path in two (current_path and new_path)
        new_path = current_path.copy()
        if ':' in rule:
            action = rule.split(':')[1]
            rule = rule.split(':')[0]
            category_to_consider = rule[0]
            conditional = rule[1]
            number_to_check = int(rule[2:])
            print('category_to_consider:',category_to_consider,'conditional:',conditional,'number_to_check:',number_to_check, 'action:', action)
            if current_path[category_to_consider]['min'] < number_to_check < current_path[category_to_consider]['max']:
                if conditional == '<':
                    if action == 'R':
                        continue
                    elif action == 'A':
                        print('action is to accept: add path to acceptable paths')
                    else:
                        new_path['path'].append(action)
                    current_path[category_to_consider]['min'] = number_to_check
                elif conditional == '>':
                    if action == 'R':
                        continue
                    elif action == 'A':
                        print('action is to accept: add path to acceptable paths')
                    else:
                        current_path['']
                    current_path[category_to_consider]['max'] = number_to_check
                print('number within range: ',current_path['path'])
                'modify path in line with conditional'
                'add other path to paths_to_explore'
            else:
                'the range is not split - the full range continues...'
                if action == 'R':
                    'remove path from paths_to_explore'
                elif action == 'A':
                    'add acceptable paths total to grand total!'
                else:
                    'move to next workflow'
        else:
            action = rule
            new_path['path'].append(action)
            
total = 0
for part in accepted_paths:
    print(part)
    for value in part.values():
        print(value)
        #total += int(value)
print('total',total)

'''
testinput: total ratings = 19114
individual ratings of 7540 for the part with x=787, 4623 for the part with x=2036, and 6951 for the part with x=2127
correct testinput obtained
correct answer obtained for Part1: 325952

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

An alternative approach could be to find all As and work backwards from there?
'''