#!/usr/bin/env python3
#https://adventofcode.com/2023/day/13

folder = '2023/'
filename = '2023_Day13_input'
extension = '.txt'
full_path = folder + filename + extension

with open(full_path) as file_object:
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
    print('evaluating candidate line:',candidate,'. iterations:',iterations)
    section_diff = 0
    for i in range(iterations):
        line_diff = 0
        line_1 = candidate - i - 1 # this counts in natural numbers - the line is the last unreflected row
        line_2 = candidate + i # this sets line_2 to start at the line below the line_1
        for j in range(len(section[0])):
            if section[line_1][j] != section[line_2][j]:
                line_diff += 1
        print('line_diff',line_diff)
        section_diff += line_diff
    print('section_diff',section_diff)
    if section_diff == 1:
        return candidate
    else:
        return 0

def find_mirror(section):
    for candidate in range(1,len(section)):
        horizontal_answer = check_candidates(section,candidate)
        if horizontal_answer:
            section_total = horizontal_answer * 100
            print('horizontal mirror found with',horizontal_answer,'columns above.')
            return section_total
    transposed_section = [''.join(row[i] for row in section) for i in range(len(section[0]))]
    for candidate in range(1,len(transposed_section)):
        section_total = check_candidates(transposed_section,candidate)
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
Correct answer obtained = 25401

test1_input should give a grand total of 400 (300 + 100)

(29846 was the right answer to part1)
'''
test_dictionary = {
    '2023_Day13_input':
    {'answer':25401},
}

from testmodule import test_function
test_function(test_dictionary,filename,grand_total)