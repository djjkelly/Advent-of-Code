#!/usr/bin/env python3
#https://adventofcode.com/2023/day/20

folder = '2023/'
filename = '2023_Day20_input'
extension = '.txt'
full_path = folder + filename + extension
total = 0
with open(full_path,'r') as file_object:
    file_content = file_object.readlines()

def consistent_split(string,delimiter):
    if delimiter in string:
        return string.split(delimiter)
    else:
        return [string]



print('total:',total)
test_dictionary = {
    '2023_Day22_input':
    {'attempts':(None),
    'low':None,'high':None,'answer':None},
    '2023_Day22_testinput':
    {'answer':5},
}

from testmodule import test_function
test_function(test_dictionary,filename,total)
'''

'''