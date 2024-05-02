#!/usr/bin/env python3
#https://adventofcode.com/2023/day/13

with open("2023/2023_Day13_test1_input.txt") as file_object:
    file_content = file_object.readlines()

sections = []
section = []
for line in file_content:
    if line == '\n':
        sections.append(section)
        section = []
    else:
        section.append(line.strip())
if section:
    sections.append(section)
# data put into list of lists, functions below

def check_candidates(section,candidate):
    print('check_candidates called. candidate:',candidate)
    for line in section:
        'print(line)'
    i1 = candidate
    i2 = len(section) - candidate
    iterations = min(i1,i2)
    print('evaluating candidate:',candidate,'. iterations:',iterations)
    candidate_viable = []
    for i in range(iterations):
        if section[candidate - i - 1] == section[candidate + i] and i > 0:
            candidate_viable.append(True)
        else:
            candidate_viable.append(False)
    if all(candidate_viable):
        return candidate

def find_mirror(section):
    for index in range(1,len(section)+1):
        horizontal_answer = check_candidates(section,index)
        if horizontal_answer:
            section_total = horizontal_answer * 100
            print('horizontal mirror found with',horizontal_answer,'columns above.')
            return section_total
    transposed_section = [''.join(row[i] for row in section) for i in range(len(section[0]))]
    for index in range(1,len(transposed_section)+1):
        section_total = check_candidates(section,index)
        if section_total:
            print('vertical mirror found with',section_total,'rows to the left.')
            return section_total

grand_total = 0
for i,section in enumerate(sections):
    print(f'\nEvaluating new section {i+1} of length {len(section)} and line length {len(section[0])}')
    section_total = find_mirror(section)
    grand_total += section_total
    print('section_total added:',section_total,'. current grand_total:',grand_total)
print('Grand total:',grand_total)
'''
test1_input should give a grand total of 400 (300 + 100)
test2_input should give a grand total of 

(29846 was the right answer to part1)
'''