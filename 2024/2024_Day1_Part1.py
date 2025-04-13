#!/usr/bin/env python3
#https://adventofcode.com/2024/day/1


folder = '2024/'
filename = '2024_Day1_input'
extension = '.txt'
full_path = folder + filename + extension
with open(full_path,'r') as file_object:
    file_content = file_object.readlines()

left_list = []
right_list = []

for line in file_content:
    left_list.append(line.split()[0])
    right_list.append(line.split()[1])

left_list_ordered = sorted(left_list)
right_list_ordered = sorted(right_list)

total = 0
for line_no,left_value in enumerate(left_list_ordered):
    right_value = right_list_ordered[line_no]
    total += abs(int(right_value) - int(left_value))
print(total)

test_dictionary = {
    '2024_Day1_input':
    {'attempts':(None,),
    'low':None,'high':29920732,'answer':None},
    '2023_Day1_testinput':
    {'answer':1722302},
}

from testmodule import test_function
test_function(test_dictionary,filename,total)
'''

'''