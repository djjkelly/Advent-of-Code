#!/usr/bin/env python3
#https://adventofcode.com/2023/day/13

with open("2023/2023_Day13_input.txt") as file_object:
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

def check_candidates(section,horizontal_candidates):
    print('check_candidates called. candidates are:',horizontal_candidates)
    for line in section:
        print(line)
    for candidate in horizontal_candidates:
        i1 = candidate - 1
        i2 = len(section) - candidate - 1
        iterations = min(i1,i2)
        print('evaluating candidate:',candidate,'. iterations:',iterations)
        candidate_viable = []
        for i in range(iterations):
            if section[candidate - i - 2] == section[candidate + i + 1]:
                candidate_viable.append(True)
            else:
                candidate_viable.append(False)
        if all(candidate_viable):
            return candidate

def find_mirror(section):
    horizontal_candidates,vertical_candidates = [],[]
    previous_string = ''
    for index,string in enumerate(section):
        if previous_string != '':
            if previous_string == string:
                number = int(index)
                horizontal_candidates.append(number)
        previous_string = string
    previous_string = ''
    answer = None
    if horizontal_candidates != []:
        answer = check_candidates(section,horizontal_candidates)
        if answer:
            section_total = answer * 100
            print('horizontal mirror found with',answer,'columns above.')
    if not answer:
        transposed_section = [''.join(row[i] for row in section) for i in range(len(section[0]))]
        for index,string in enumerate(transposed_section):
            if previous_string != '':
                if previous_string == string:
                    number = int(index)
                    vertical_candidates.append(number)
            previous_string = string
    if vertical_candidates != []:
        vertical_candidate = check_candidates(transposed_section,vertical_candidates)
        if vertical_candidate:
            section_total = vertical_candidate
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
test1_input should give a grand total of 405 (5 + 400)
test2_input should give a grand total of 1700

18094 is not the right answer - too low.
24655 is not the right answer - too low.
32497 is not the right answer.
28155 is not the right answer.
29843 is not the right answer.
29846 is the right answer!
'''