#!/usr/bin/env python3
#https://adventofcode.com/2023/day/13

with open("2023/2023_Day13_testinput.txt",'r') as file_object:
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
def min_ignore_negative(i1,i2):
    if i1 < 0:
        i1 = 0
    if i2 < 0:
        i2 = 0
    iterations = min(i1,i2)
    return iterations

def check_horizontal(section,horizontal_candidates):
    print('check_horizontal called. candidates are:',horizontal_candidates)
    for candidate in horizontal_candidates:
        i1 = candidate - 1
        i2 = len(section) - candidate - 1
        #print('i1:',i1,'i2:',i2)
        iterations = min_ignore_negative(i1,i2)
        candidate_viable = False
        for i in range(iterations):
            #print('i =',i)
            if section[candidate - i - 2] == section[candidate + i + 1]:
                candidate_viable = True
            else:
                candidate_viable = False
        if candidate_viable:
            #print('horizontal answer found!',candidate)
            return candidate
#print('test of check_horizontal:',check_horizontal(sections[1],[4])) # should compare two pairs of lines when input is 4.

def check_vertical(section,vertical_candidates):
    print('check_vertical called. candidates are:',vertical_candidates)
    for candidate in vertical_candidates:
        print('evaluating vertical candidate: ',candidate)
        i1 = candidate - 1
        i2 = len(section[0]) - candidate - 1
        iterations = min_ignore_negative(i1,i2)
        print('iterations:',iterations)
        candidate_viable = False
        for i in range(iterations):
            print('i =',i)
            for j in range(len(section)):
                if section[j][candidate - i - 2] == section[j][candidate + i + 1]:
                    candidate_viable = True
                else:
                    candidate_viable = False
                    break
        if candidate_viable:
            print('vertical answer found!',candidate)
            return candidate
#print('test of check_vertical (should compare 3 pairs):',check_vertical(sections[0],[5]))

def find_mirror(section):
    previous_string = ''
    vert_bool = [True for l in range(len(section[0]))]
    horizontal_candidates,vertical_candidates = [],[]
    for index,string in enumerate(section):
        if previous_string != '':
            if previous_string == string:
                number = int(index)
                print('horizontal mirror candidate found: index: ',number)
                horizontal_candidates.append(number)
            else:
                previous_char = ''
                for char_no,char in enumerate(string):
                    if vert_bool[char_no]:
                        if char != previous_char:
                            vert_bool[char_no] = False
                    previous_char = char
        previous_string = string
    for bool_no in range(len(vert_bool)):
        if vert_bool[bool_no]:
            number = int(bool_no)
            print('vertical mirror candidate found. index: ',number)
            vertical_candidates.append(number)
    print('horizontal_candidates:',horizontal_candidates,'vertical_candidates:', vertical_candidates)
    if horizontal_candidates != []:
        horizontal_candidate = check_horizontal(section,horizontal_candidates)
        if horizontal_candidate:
            answer = horizontal_candidate
            orientation = 'horizontal'
    if vertical_candidates != []:
        vertical_candidate = check_vertical(section,vertical_candidates)
        if vertical_candidate:
            answer = vertical_candidate
            orientation = 'vertical'
    print(orientation,'mirror found!',answer)
    return answer,orientation

'''for section in sections:
    print('\nNew section!')
    find_mirror(section)'''

def summarise_section(section):
    '''to summarise a section, either:
            add up the number of columns to the left of the vertical line of reflection
            add up the number of columns above the horizontal line of reflection * 100
       note that the complete reflection doesn't have to appear in the '''
    print("SUMMARISING SECTION")
    number,orientation = find_mirror(section)
    if orientation == 'horizontal':
        number = number * 100
    return number

grand_total = 0
for section in sections:
    section_total = summarise_section(section)
    grand_total += section_total
print(grand_total)
'''
test_input should give a grand total of 405 (5 + 400)

'''