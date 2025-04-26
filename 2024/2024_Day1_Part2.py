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

right_list_counts = {}
for right_value in right_list:
    if right_value not in right_list_counts:
        right_list_counts[right_value] = 1
    else:
        right_list_counts[right_value] += 1

total = 0
for left_value in left_list:
    if left_value in right_list_counts:
        right_value_count = right_list_counts[left_value]
        total += right_value_count * int(left_value)
print(total)

test_dictionary = {
    '2024_Day1_input':
    {'attempts':(None,),
    'low':None,'high':None,'answer':20373490},
    
    '2023_Day1_testinput':
    {'answer':None},
}

from testmodule import test_function
test_function(test_dictionary,filename,total)
'''

'''