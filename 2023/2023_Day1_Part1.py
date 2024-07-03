#!/usr/bin/env python3
# https://adventofcode.com/2023/day/1

folder = '2023/'
filename = '2023_Day1_input'
extension = '.txt'
full_path = folder + filename + extension

import codecs
with codecs.open(full_path) as file:
    total = 0
    for line in file:
        for char in line:
            if char.isnumeric():
                first_digit = char
                break
        reversed_line = line[::-1]
        for char in reversed_line:
            if char.isnumeric():
                last_digit = char
                break
        total += int(first_digit+last_digit)
print (total)
print("done")

'''
55538 is my answer
'''
test_dictionary = {
    '2023_Day1_input':
    {'answer':55538},
}

from testmodule import test_function
test_function(test_dictionary,filename,total)