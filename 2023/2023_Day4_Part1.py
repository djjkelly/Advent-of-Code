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

total_score = 0
for line_number,line in enumerate(file_content,start=1):
    line = line.split(":")[1].strip()
    winning_numbers = line.split("|")[0].split()
    numbers_held = line.split("|")[1].split()
    print(f"{line_number}\n{winning_numbers}\n{numbers_held}")
    
    matching = 0
    for number in winning_numbers:
        if number in numbers_held:
            matching += 1
    print(f'{matching} matching cards found')

    line_score = 0
    if matching >= 1:
        line_score = 2**(matching-1)
    total_score += line_score
    print(f"Line score is: {line_score}")
print(total_score)
test_dictionary = {
    '2023_Day4_input':
    {'answer':21919},
}

from testmodule import test_function
test_function(test_dictionary,filename,total_score)