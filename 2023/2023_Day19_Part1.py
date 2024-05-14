#!/usr/bin/env python3
#https://adventofcode.com/2023/day/19

with open("2023/2023_Day19_testinput.txt",'r') as file_object:
    file_content = file_object.readlines()
    before_line_break = True
    workflows = {}
    part_ratings = []
    for line in file_content:
        if line == '\n':
            before_line_break = False
            continue
        line = line.strip()
        if before_line_break:
            workflow_name = line.split('{')[0]
            rules = line.split('}')[0].split('{')[1].split(',')
            workflows[workflow_name] = rules
        else:
            split_ratings = line.split('}')[0].split(',')
            line_ratings = {'x':split_ratings[0].split('=')[1],'m':split_ratings[1].split('=')[1],'a':split_ratings[2].split('=')[1],'s':split_ratings[3].split('=')[1]}
            part_ratings.append(line_ratings)

def process_action(action):
    part_accepted = None
    next_workflow = None
    if action == 'R':
        part_accepted = False
    elif action == 'A':
        part_accepted = True
    else:
        next_workflow = action
    return part_accepted,next_workflow

def process_workflow(part,current_workflow):
    for rule in current_workflow:
        if ':' in rule:
            action = rule.split(':')[1]
            rule = rule.split(':')[0]
            category_to_consider = rule[0]
            part_rating = part[category_to_consider]
            conditional = rule[1]
            number_to_check = rule[2:]
            print('category_to_consider:',category_to_consider,'conditional:',conditional,'number_to_check:',number_to_check, 'action:', action)
            if conditional == '<':
                if part_rating < number_to_check:
                    part_accepted,next_workflow = process_action(action)
                    return part_accepted,next_workflow
                else:
                    continue
            elif conditional == '>':
                if part_rating > number_to_check:
                    part_accepted,next_workflow = process_action(action)
                    return part_accepted,next_workflow
                else:
                    continue
        else:
            action = rule
            part_accepted,next_workflow = process_action(action)
        return part_accepted,next_workflow

accepted_parts = []
for part in part_ratings:
    current_workflow_name = 'in'
    part_accepted = None
    current_workflow = workflow_name[current_workflow_name]
    while True:
        current_workflow = workflow_name[current_workflow_name]
        part_accepted,current_workflow_name = process_workflow(part,current_workflow)
        if part_accepted is True:
            accepted_parts.append(part)
            break
        elif part_accepted is False:
            print('FALSE!')
            break

total = 0
for part in accepted_parts:
    print(part)
    for value in part.values():
        print(value)
        total += int(value)
print('total',total)

'''
testinput: total ratings = 19114
individual ratings of 7540 for the part with x=787, 4623 for the part with x=2036, and 6951 for the part with x=2127

'''