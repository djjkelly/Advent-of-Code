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
#print("test - should print 53. Answer: ",find_middle_page([97,61,53,29,13]))

def updates_follow_rule(update,rule):
    first_number,second_number = rule
    for i in range(len(update)-1):
        page_no = update[i]
        if first_number == page_no:
            return True
        if second_number == page_no:
            return False
    return True
#print(updates_follow_rule([1,2,3,4,5,47,53],[47,53]))

total = 0
for update in updates:
    updates_follow_rules = True
    for rule in rules:
        if rule_applicable(update,rule):
            if updates_follow_rule(update,rule):
                continue
            else:
                updates_follow_rules = False
                break
    if updates_follow_rules:
        middle_page_no = find_middle_page(update)
        total += middle_page_no
print(total)

test_dictionary = {
    '2024_Day5_testinput':
    {'attempts':(None,),
    'low':None,'high':None,'answer':5129},

    '2024_Day5_testinput':
    {'answer':143},
}

from testmodule import test_function
test_function(test_dictionary,filename,total)
'''

'''