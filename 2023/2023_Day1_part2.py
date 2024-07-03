#!/usr/bin/env python3
# https://adventofcode.com/2023/day/1

folder = '2023/'
filename = '2023_Day1_input'
extension = '.txt'
full_path = folder + filename + extension

num_dict = {
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9',
    }

with open(full_path) as file:
    total = 0
    for line in file:
        print(line.strip())
        position_dict = {
            '1':None,
            '2':None,
            '3':None,
            '4':None,
            '5':None,
            '6':None,
            '7':None,
            '8':None,
            '9':None,
            }
        reversed_dict = position_dict.copy()
        reversed_line = line[::-1]

        # find the first numerical character in the string:
        position=0
        for char in line:
            position+=1
            if char.isnumeric() and position_dict[char]==None:
                position_dict[char] = position-1
                break

        # find the first number written in alphabetic characters:
        for alphabetic_key,value in num_dict.items():
            position = line.find(alphabetic_key)
            key=num_dict[alphabetic_key]
            if position > -1 and position_dict[key]==None:
                position_dict[key] = position
            elif position >-1 and position < position_dict[key]:
                position_dict[key] = position            

        # find the earliest position of any number appearing in the string, written in either format
        earliest_position = float('inf')
        for key in position_dict:
            value = position_dict[key]
            if value is None:
                continue
            if int(value) < earliest_position:
                earliest_position = int(value)
                first_digit = key

        # find the first numerical character in the REVERSED string
        position=0
        for char in reversed_line:
            position+=1
            if char.isnumeric() and reversed_dict[char] is None:
                reversed_dict[char] = position-1
                break

        # find the first number written in alphabetic characters in the REVERSED STRING
        for alphabetic_key,value in num_dict.items():
            position = reversed_line.find(alphabetic_key[::-1])
            key=num_dict[alphabetic_key]
            if position > -1 and reversed_dict[key] is None:
                reversed_dict[key] = position
            elif position >-1 and position < reversed_dict[key]:
                reversed_dict[key] = position

        # find the last position of any number appearing in the string, written in either format
        last_position = float('inf')
        for key in reversed_dict:
            value = reversed_dict[key]
            if value is None:
                continue
            if int(value) < last_position:
                last_position = int(value)
                last_digit = key

        subtotal = first_digit + last_digit
        print(subtotal + '\n')
        total += int(subtotal)
print (total)
'''
54875 is my answer
'''
test_dictionary = {
    '2023_Day1_input':
    {'answer':54875},
}

from testmodule import test_function
test_function(test_dictionary,filename,total)