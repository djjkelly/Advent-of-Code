#!/usr/bin/env python3
#https://adventofcode.com/2023/day/16

with open("2023/2023_Day16_testinput.txt",'r') as file_object:
    file_content = file_object.readlines()
content_list=[]
for line in file_content:
    line = line.strip()
    new_line = []
    for char in line:
        new_line.append(char) # this puts \\ instead of \
    content_list.append(new_line)
    print(new_line)

'''
. means transparent

/ turns right to up, left to down, down to left, up to right
(left and down swap, up and right swap)

\ turns right to down, left to up, down to right, up to left - in other words left and up sw
(left and up swap, down and right swap)

splitter - or | means nothing when hit by a beam end-on.
when hit side on, the beam is split into both perpendicular directions.

LIGHT BEAM enters from left, in top-left corner.
'''



energised_tiles_no = 0

'''
testinput should give a number of energised tiles of: 46

'''