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

def check_candidates(section,horizontal_candidates):
    print('check_candidates called. candidates are:',horizontal_candidates)
    for line in section:
        print(line)
    for candidate in horizontal_candidates:
        i1 = candidate - 1
        i2 = len(section) - candidate - 1
        iterations = min(i1,i2)
        print('evaluating candidate:',candidate,'. iterations:',iterations)
        if iterations == 0:
            print("-----------------------ZERO ITERATIONS REQUIRED")
            return candidate
        candidate_viable = []
        for i in range(iterations):
            if section[candidate - i - 2] == section[candidate + i + 1]:
                candidate_viable.append(True)
            else:
                candidate_viable.append(False)
        if all(candidate_viable):
            return candidate

def find_mirror(section):
    previous_string = ''
    vert_bool = [None for l in range(len(section[0]))]
    horizontal_candidates,vertical_candidates = [],[]
    for index,string in enumerate(section):
        if previous_string != '':
            if previous_string == string and index >0:
                number = int(index)
                horizontal_candidates.append(number)
            else:
                previous_char = ''
                for char_no,char in enumerate(string):
                    if vert_bool[char_no] is not None:
                        if char == previous_char:
                            vert_bool[char_no] = True
                        else:
                            vert_bool[char_no] = False
                    previous_char = char
        previous_string = string
    for bool_no in range(len(vert_bool)):
        if vert_bool[bool_no]:
            number = int(bool_no)
            vertical_candidates.append(number)
    #print('horizontal_candidates:',horizontal_candidates,'vertical_candidates:', vertical_candidates)
    horizontal_candidate = None
    if horizontal_candidates != []:
        horizontal_candidate = check_candidates(section,horizontal_candidates)
        if horizontal_candidate:
            answer = horizontal_candidate * 100
            print('horizontal mirror found with',horizontal_candidate,'columns above.')
    if vertical_candidates != []:
        transposed_section = [''.join(row[i] for row in section) for i in range(len(section[0]))]
        vertical_candidate = check_candidates(transposed_section,vertical_candidates)
        if vertical_candidate:
            answer = vertical_candidate
            print('vertical mirror found with',answer,'rows to the left.')
    if vertical_candidates != [] and horizontal_candidates != [] and vertical_candidate and horizontal_candidate:
        print('------------------------------------------------------------------------DOUBLE TROUBLE!')
    return answer

grand_total = 0
for i,section in enumerate(sections):
    print(f'\nEvaluating new section {i+1} of length {len(section)} and line length {len(section[0])}')
    section_total = find_mirror(section)
    grand_total += section_total
    print('section_total added:',section_total,'. current grand_total:',grand_total)
print('Grand total:',grand_total)
'''
test_input should give a grand total of 405 (5 + 400)

18094 is not the right answer - too low.
24655 is not the right answer - too low.
32497 is not the right answer.
28155 is not the right answer.
29843 is not the right answer.

'''