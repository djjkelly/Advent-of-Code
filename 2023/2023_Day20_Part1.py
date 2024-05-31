#!/usr/bin/env python3
#https://adventofcode.com/2023/day/21

folder = '2023/'
filename = '2023_Day20_test1_input'
extension = '.txt'
full_path = folder + filename + extension
total = 0
with open(full_path,'r') as file_object:
    file_content = file_object.readlines()

modules = {}

def consistent_split(string,delimiter):
    if delimiter in string:
        return string.split(delimiter)
    else:
        return [string]

for line_no,line in enumerate(file_content):
    split_line = line.strip().split(' -> ')
    if split_line[0] == r'broadcaster':
        broadcaster_destinations = consistent_split(split_line[1],', ')
    elif split_line[0][0] == r'%':
        module_type = r'flip-flop'
        module_name = split_line[0][1:]
        destinations = consistent_split(split_line[1],', ')
        modules[module_name] = {'type':module_type,'destinations':destinations,'state':'off'}
    elif split_line[0][0] == r'&':
        module_type = r'conjunction'
        module_name = split_line[0][1:]
        destinations = consistent_split(split_line[1],', ')
        modules[module_name] = {'type':module_type,'destinations':destinations,'memory':'low'}
for item in modules.items():
    print(item)

def send_pulses(button_pushes):
    for push in range(1,button_pushes+1):
        if push == 1000:
            print(push)
    return total

button_pushes = 1000
total = send_pulses(button_pushes)
print('total:',total)
test_dictionary = {
    '2023_Day20_input':
    {'attempts':(None),
    'low':None,'high':None,'answer':None},
    '2023_Day20_test1_input':
    {'attempts':(None),
    'answer':32000000},
    '2023_Day20_test2_input':
    {'attempts':(None),
    'answer':11687500},
}

from testmodule import test_function
test_function(test_dictionary,filename,total)
'''

'''