#!/usr/bin/env python3
#https://adventofcode.com/2023/day/9

with open("2023/2023_Day9_input.txt") as file_object:
    file_content = file_object.readlines()

test_content = ['0 3 6 9 12 15','1 3 6 10 15 21','10 13 16 21 30 45']
#file_content = test_content # TEST INPUT !

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

total_values = 0
for history in histories:
    print('New history commencing:\n',history)
    numbers = history
    all_numbers_are_zero = False
    diffs_array = [numbers]
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
        else:
            numbers = diffs
    #print(diffs_array)
    diffs_array_indices = range(len(diffs_array)-1,-1,-1)
    value_below = 0
    for diffs_array_index in diffs_array_indices:
        value_left = diffs_array[diffs_array_index][-1]
        predicted_value = value_left + value_below
        #print(f'predicted_value: {predicted_value}, consisting of left ({value_left}) and below ({value_below})')
        value_below = predicted_value
    print('Prediction for this history: ',predicted_value)
    total_values += predicted_value
print(f'Final answer: total values = {total_values}')
'''

'''