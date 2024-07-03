#!/usr/bin/env python3
#https://adventofcode.com/2023/day/4

folder = '2023/'
filename = '2023_Day4_input'
extension = '.txt'
full_path = folder + filename + extension

try:
    with open(full_path) as file_object:
        file_content = file_object.readlines()
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"An error was encountered: {e}")

copies = [1]*len(file_content)

total_score = 0
for line_number,line in enumerate(file_content,start=1):
    line = line.split(":")[1].strip()
    winning_numbers = line.split("|")[0].split()
    numbers_held = line.split("|")[1].split()
    #print(f"{line_number}\n{winning_numbers}\n{numbers_held}")
    
    matching = 0
    for number in winning_numbers:
        if number in numbers_held:
            matching += 1
    print(f'{matching} matching cards found on line {line_number}')

    for i in range(matching):
        copies[line_number+i] += copies[line_number-1]
print(copies)

for element in copies:
    total_score += element
print(total_score)

'''
line 1: 4 cards, one copy added to 2, 3, 4, 5.
9881048 is right
41205469555 is a bit too high ha ha - this was a result of forgetting to subtract 1 from the line number in the for loop.
'''
test_dictionary = {
    '2023_Day4_input':
    {'answer':9881048},
}

from testmodule import test_function
test_function(test_dictionary,filename,total_score)