#!/usr/bin/env python3
#https://adventofcode.com/2024/day/4

folder = '2024/'
filename = '2024_Day5_input'
extension = '.txt'
full_path = folder + filename + extension
with open(full_path,'r') as file_object:
    file_content = file_object.readlines()

rules = []
updates = []

section_number = 1
for line in file_content:
    line = line.strip()
    if line == '':
        section_number += 1
        continue
    if section_number == 1:
        rule = line.split('|')
        rule = list(map(int,rule))
        rules.append(rule)
    elif section_number == 2:
        update = line.split(',')
        update = list(map(int,update))
        updates.append(update)

def rule_applicable(update,rule):
    a,b = rule[0],rule[1]
    if a in update and b in update:
        return True
    else:
        return False

def find_middle_page(pages):
    middle_page_no = pages[len(pages)//2]
    return middle_page_no

def update_follows_rule(update,rule):
    first_number,second_number = rule
    for i in range(len(update)-1):
        page_no = update[i]
        if first_number == page_no:
            return True
        if second_number == page_no:
            return False
    return True

def update_follows_all_rules(update,rules):
    for rule in rules:
        if not update_follows_rule(update,rule):
            return False
    else:
        return True

#reformat the data to look a bit nicer
all_broken_rules = []
all_broken_updates = []
for update in updates:
    rules_broken = []
    for rule in rules:
        if rule_applicable(update,rule):
            if update_follows_rule(update,rule):
                continue
            else:
                rules_broken.append(rule)
                continue
    if rules_broken != []:
        all_broken_rules.append(rules_broken)
        all_broken_updates.append(update)
#print(all_broken_rules)
#print(all_broken_updates)

total = 0
for i,broken_update in enumerate(all_broken_updates):
    broken_rules = all_broken_rules[i]
    while_count = 0
    while True:
        while_count += 1
        if while_count % 1000 == 0:
            print(while_count)
        for rule in broken_rules:
            a,b = rule
            x,y = broken_update.index(a),broken_update.index(b)
            broken_update[x],broken_update[y] = broken_update[y],broken_update[x]
        if update_follows_all_rules(broken_update,broken_rules):
            total += find_middle_page(broken_update)
            break
print("Total:",total)

'''
Test data can be solved by swapping any incorrect values in pairs.
The real data forms loops which don't resolve when undertaking this approach.
A better sorting algorithm is needed.
Some lines in the data are 23 characters long.

A clue from the problem statement - there is only ONE right order per update.
'''

test_dictionary = {
    '2024_Day5_testinput':
    {'attempts':(None,),
    'low':None,'high':None,'answer':None},

    '2024_Day5_testinput':
    {'answer':123},
}

from testmodule import test_function
test_function(test_dictionary,filename,total)
'''

'''