#!/usr/bin/env python3
#https://adventofcode.com/2023/day/9

with open("2023/2023_Day9_input.txt") as file_object:
    file_content = file_object.readlines()

test_content = ['0 3 6 9 12 15','1 3 6 10 15 21','10 13 16 21 30 45']
file_content = test_content # TEST INPUT !

histories = []
for line in file_content:
    line = line.strip()
    line = line.split()
    integers = []
    for number in line:
        integer = int(number)
        integers.append(integer)
    histories.append(integers)
print(histories)

for history in histories:
    print(history)
    numbers = history
    all_numbers_are_zero = False
    diffs_array = []
    while not all_numbers_are_zero:
        previous_number = None
        diffs = []
        for number in numbers:
            if previous_number is not None:
                diff = number - previous_number
                diffs.append(diff)
            previous_number = number
        print(diffs)
        diffs_array.append(diffs)
        if all(n == 0 for n in diffs):
            all_numbers_are_zero = True
            print('all numbers are zero - finishing this history')
        else:
            numbers = diffs
'''

'''