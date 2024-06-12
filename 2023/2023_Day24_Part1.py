#!/usr/bin/env python3
#https://adventofcode.com/2023/day/24

folder = '2023/'
filename = '2023_Day24_testinput'
extension = '.txt'
full_path = folder + filename + extension
with open(full_path,'r') as file_object:
    file_content = file_object.readlines()
total = 0
input_list = []
for line in file_content:
    line = line.strip()
    input_list.append(line)


print('total:',total)
test_dictionary = {
    '2023_Day24_input':
    {'attempts':(None),
    'low':None,'high':None,'answer':None},
    '2023_Day24_testinput':
    {'answer':2},
}

from testmodule import test_function
test_function(test_dictionary,filename,total)
'''


'''