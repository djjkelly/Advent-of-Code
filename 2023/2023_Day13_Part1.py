#!/usr/bin/env python3
#https://adventofcode.com/2023/day/13

with open("2023/2023_Day13_input.txt",'r') as file_object:
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

def find_mirror(section):
    previous_string = ''
    for index,string in enumerate(section):
        if previous_string != '':
            if previous_string == string:
                number = index
                orientation = 'horizontal'
    return number, orientation


def summarise_section(section):
    '''to summarise a section, either:
            add up the number of columns to the left of the vertical line of reflection
            add up the number of columns above the horizontal line of reflection * 100
       note that the complete reflection doesn't have to appear in the '''
    number,orientation = find_mirror(section)
    if orientation == 'horizontal':
        number = number * 100
    return number

grand_total = 0
for section in sections:
    section_total = summarise_section(section)
    grand_total += section_total
'''
test_input should give a grand total of 405 (5 + 400)

'''