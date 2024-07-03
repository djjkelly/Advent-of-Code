#!/usr/bin/env python3
#https://adventofcode.com/2023/day/15

folder = '2023/'
filename = '2023_Day15_input'
extension = '.txt'
full_path = folder + filename + extension

with open(full_path,'r') as file_object:
    file_content = file_object.readlines()

file_list = file_content[0].strip().split(',')

def HASH(string):
    current_value = 0
    for char in string:
        code = ord(char)
        print('code:',code)
        current_value += code
        current_value = (current_value * 17) % 256
        print('updated value:', current_value)
    return current_value

total = 0
for step in file_list:
    print('step:',step)
    hash = HASH(step)
    print('hash:',hash)
    total += hash

print(total)

'''
testinput should have a result of 1320
Correct answer found: 516657
'''
test_dictionary = {
    '2023_Day15_input':
    {'answer':516657},
}

from testmodule import test_function
test_function(test_dictionary,filename,total)