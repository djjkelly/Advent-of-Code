#!/usr/bin/env python3
#https://adventofcode.com/2024/day/4

folder = '2024/'
filename = '2024_Day4_testinput'
extension = '.txt'
full_path = folder + filename + extension
with open(full_path,'r') as file_object:
    file_content = file_object.readlines()

rows = len(file_content)

transformed_table = [['' for x in range(rows)]for y in range(rows)]

total = 0
import re
search_string = "XMAS|SAMX"
for line_no,line in enumerate(file_content):
    line = line.strip()
    for char_no,char in enumerate(line):
        transformed_table[char_no][line_no] = char
    list = re.findall(search_string,line)
    total += len(list)

for line in transformed_table:
    line = ''.join(line)
    list = re.findall(search_string,line)
    total += len(list)

diagonals = []
for line_no,line in enumerate(file_content):
    line = line.strip()
    for i in range(line_no):
        print(i)
    newline = line[rows - line_no ::]
    diagonals.append(newline)

transformed_diagonals = []
for line_no,line in enumerate(transformed_table):
    newline = line[rows - line_no ::]
    diagonals.append(newline)

'''
Need to get the diagonals right...
[0][9]
[0][8]  [1][9]
[0][7]  [1][8]  [2][9]
'''

for line in diagonals:
    line = ''.join(line)
    list = re.findall(search_string,line)
    total += len(list)

for line in transformed_diagonals:
    line = ''.join(line)
    list = re.findall(search_string,line)
    total += len(list)

print(total)

test_dictionary = {
    '2024_Day4_input':
    {'attempts':(None,),
    'low':None,'high':None,'answer':None},

    '2024_Day4_testinput':
    {'answer':18},
}

from testmodule import test_function
test_function(test_dictionary,filename,total)
'''

'''