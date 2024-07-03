#!/usr/bin/env python3
#https://adventofcode.com/2023/day/15

import re

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
        current_value += code
        current_value = (current_value * 17) % 256
    return current_value

def subtract_lens(step):
    label = re.split('[-=]',step)[0]
    box_number = HASH(label)
    print(f'subtracting label "{label}" in box number "{box_number}".')
    for slot_no,slot in enumerate(box_list[box_number]):
        if label in slot:
            del box_list[box_number][slot_no]

def set_lens(step):
    label = re.split('[-=]',step)[0]
    box_no = HASH(label)
    focal_length = step.split('=')[1]
    print(f'setting label "{label}" with focal length "{focal_length}" in box number "{box_no}".')
    slot_replaced = False
    for slot_no,slot in enumerate(box_list[box_no]):
        if label in slot:
            box_list[box_no][slot_no][label] = focal_length
            slot_replaced = True
    if not slot_replaced:
        box_list[box_no].append({label:focal_length})

box_list = [[] for _ in range(256)] # correction - the multiplication symbol refers to the same list object 256 times
total_focusing_power = 0
for step in file_list:
    print('step:',step)
    if '-' in step:
        print('\'-\' found. Subtract lens!')
        subtract_lens(step)
    elif '=' in step:
        print('\'=\' found. Setting lens!')
        set_lens(step)
    print('box_list:', box_list)
for box_no,box in enumerate(box_list):
    for slot_no,slot in enumerate(box):
        focal_length = int(next(iter(slot.values())))
        lens_power = (box_no+1) * (slot_no+1) * (focal_length)
        print('lens_power',lens_power)
        total_focusing_power += lens_power
print(total_focusing_power)

'''
testinput should give 1, 4, 28, 40, 72 and have a result of 145
Correct answer obtained - 210906

The - symbol means a lens is removed.
Subsequent lenses will be moved 'forwards' when this happens (to a lower list index).

The = symbol sets a lens.
If one is already there WITH THE SAME LABEL, the old lens is removed and the new one put in its place.
If not it goes to the 'back' of all the existing lenses (last index + 1).

Only one copy of a given label can exist in a given box.
Each label will always evaluate to the same box (HASH works the same time each time)
'''
test_dictionary = {
    '2023_Day15_input':
    {'answer':210906},
}

from testmodule import test_function
test_function(test_dictionary,filename,total_focusing_power)