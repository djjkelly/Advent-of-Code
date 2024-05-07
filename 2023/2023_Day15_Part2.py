#!/usr/bin/env python3
#https://adventofcode.com/2023/day/15

import re

with open("2023/2023_Day15_testinput.txt",'r') as file_object:
    file_content = file_object.readlines()

file_list = file_content[0].strip().split(',')

def HASH(string):
    current_value = 0
    for char in string:
        code = ord(char)
        current_value += code
        current_value = (current_value * 17) % 256
    return current_value

def subtract_lens(label):
    print(f'subtracting label "{label}"')

def set_lens(label):
    print(f'setting label "{label}"')

box_list = [[]] * 256
label_dict = {}
total_focusing_power = 0
for step in file_list:
    print('step:',step)
    label = re.split('-=',step)[0]
    box_number = HASH(label)
    print('box_number:',box_number)
    if '-' in step:
        print('\'-\' found. Subtract lens!')
        subtract_lens(label)
    elif '=' in step:
        print('\'=\' found. Setting lens!')
        focal_length = int(step.split('=')[1])
        set_lens(step)
    print('label_dict:',label_dict)
    print('box_list:', box_list)

print(total_focusing_power)

'''
testinput should give 1, 4, 28, 40, 72 and have a result of 145

The - symbol means a lens is removed.
Subsequent lenses will be moved 'forwards' when this happens (to a lower list index).

The = symbol sets a lens.
If one is already there, the old lens is removed and the new one put in its place.
If not it goes to the 'back' of all the existing lenses (last index + 1).
'''