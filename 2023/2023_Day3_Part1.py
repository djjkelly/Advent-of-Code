#!/usr/bin/env python3
#https://adventofcode.com/2023/day/3

folder = '2023/'
filename = '2023_Day3_input'
extension = '.txt'
full_path = folder + filename + extension

try:
    with open(full_path) as file_object:
        file_content = file_object.readlines()
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"An error was encountered: {e}")

symbols = "!@£$%^&*()-=_+|/\\#"

total = 0

for line_number in range(len(file_content)):
    subtotal = 0
    
    current_line = file_content[line_number].strip()
    if line_number < len(file_content)-1:
        next_line = file_content[line_number + 1].strip()
    else:
        next_line = ''
        for character in current_line:
            next_line += '.'
    if line_number == 0:
        previous_line = ''
        for character in current_line:
            previous_line += '.'

    print(previous_line)
    print(current_line)
    print(next_line)
    
    working_number = ''
    next_numbers_are_eligible = False
    for index,character in enumerate(current_line):
        symbol_on_nearby_line = False
        
        if previous_line[index] in symbols or next_line[index] in symbols:
            symbol_on_nearby_line = True
        else:
            if index > 0:
                if previous_line[index-1] in symbols or next_line[index-1] in symbols:
                    symbol_on_nearby_line = True
            if index < len(current_line)-1:
                if previous_line[index+1] in symbols or next_line[index+1]in symbols:
                    symbol_on_nearby_line = True

        if character.isnumeric():
            working_number += character
            if symbol_on_nearby_line:
                next_numbers_are_eligible = True
        elif character in symbols:
            if working_number != '':
                subtotal += int(working_number)
                print('Part number ' + str(working_number) + ' found!')
            working_number = ''
            next_numbers_are_eligible = True

        else:
            if next_numbers_are_eligible:
                if working_number != '':
                    subtotal += int(working_number)
                    print('Part number ' + str(working_number) + ' found!')
                next_numbers_are_eligible = False
            working_number = ''
    if next_numbers_are_eligible:
        if working_number != '':
            subtotal += int(working_number)
            print('Part number ' + str(working_number) + ' found!')
            next_numbers_are_eligible = False
            working_number = ''
    
    previous_line = current_line
    print ("Subtotal for line " + str(line_number) + " is " + str(subtotal))
    total += subtotal

"""
Subtotals expected:
Line 1: 305 + 124 + 514 = 943
Line 2: 113 + 901 + 869 + 257 = 2140
Line 3: 377 + 783 + 9 + 855 + 940 + 463 + 844 + 679 = 4950

"""
print(total)
test_dictionary = {
    '2023_Day3_input':
    {'answer':550934},
}

from testmodule import test_function
test_function(test_dictionary,filename,total)