#!/usr/bin/env python3
#https://adventofcode.com/2024/day/3

folder = '2024/'
filename = '2024_Day3_input'
extension = '.txt'
full_path = folder + filename + extension
with open(full_path,'r') as file_object:
    file_content = file_object.readlines()

import re

status_active = True
total = 0
for line in file_content:
    regex_list = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)|(?=(do\(\)|don't\(\)))",line)
    for x,y,z in regex_list:
        if z == '':
            if status_active:
                total += int(x)*int(y)
        elif z == "do()":
            status_active = True
        elif z == "don't()":
            status_active = False
print(total)

test_dictionary = {
    '2024_Day3_input':
    {'attempts':(None,),
    'low':None,'high':None,'answer':82868252},

    '2024_Day3_testinput':
    {'answer':48},
}

from testmodule import test_function
test_function(test_dictionary,filename,total)
'''

'''