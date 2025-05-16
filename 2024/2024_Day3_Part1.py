#!/usr/bin/env python3
#https://adventofcode.com/2024/day/3

folder = '2024/'
filename = '2024_Day3_input'
extension = '.txt'
full_path = folder + filename + extension
with open(full_path,'r') as file_object:
    file_content = file_object.readlines()

lines = []

total = 0

test_dictionary = {
    '2024_Day3_input':
    {'attempts':(None,),
    'low':None,'high':None,'answer':717},

    '2024_Day3_testinput':
    {'answer':161},
}

from testmodule import test_function
test_function(test_dictionary,filename,total)
'''

'''