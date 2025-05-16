#!/usr/bin/env python3
#https://adventofcode.com/2024/day/2


folder = '2024/'
filename = '2024_Day2_input'
extension = '.txt'
full_path = folder + filename + extension
with open(full_path,'r') as file_object:
    file_content = file_object.readlines()

lines = []

for line in file_content:
    line = line.strip()
    line = line.split()
    new_line = []
    for value in line:
        new_line.append(int(value))
    lines.append(new_line)

total = 0
for line in lines:
    line_valid = True
    increasing_or_decreasing = None
    previous_value = None
    for value in line:
        if previous_value == None:
            previous_value = value
            continue
        if value - previous_value == 0:
            line_valid = False
            break
        if abs(value - previous_value) > 3:
            line_valid = False
            break
        if value - previous_value < 0:
            if increasing_or_decreasing == 'increasing':
                line_valid = False
                break
            increasing_or_decreasing = 'decreasing'
        if value - previous_value > 0:
            if increasing_or_decreasing == 'decreasing':
                line_valid = False
                break
            increasing_or_decreasing = 'increasing'
        previous_value = value
    if line_valid:
        total += 1
print(total)

test_dictionary = {
    '2024_Day2_input':
    {'attempts':(None,),
    'low':None,'high':None,'answer':686},

    '2024_Day2_testinput':
    {'answer':2},
}

from testmodule import test_function
test_function(test_dictionary,filename,total)
'''

'''