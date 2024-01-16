#!/usr/bin/env python3
# https://adventofcode.com/2023/day/1

import codecs
with codecs.open("2023/2023_Day1_input.txt") as file:
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