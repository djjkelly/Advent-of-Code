#!/usr/bin/env python3
#https://adventofcode.com/2023/day/3

try:
    with open("2023_Day3_input.txt") as file_object:
        file_content = file_object.readlines()
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"An error was encountered: {e}")

symbols = "!@£$%^&*()-=_+|/\\#"

total = 0

for line_number in range(len(file_content)):
    current_line = file_content[line_number].strip()
    if line_number != len(file_content):
        next_line = file_content[line_number + 1].strip()
    else:
        next_line = ''
        for character in range(len(current_line)):
            next_line.append('.')
    if line_number > 0:
        previous_line = 
    next_to_part = [False]*len(current_line)
    current_number = ''
    subtotal = 0
    
    for char in range(len(current_line)):
        if current_line[char] in symbols:
            print("Symbol on current line at character " + str(char) + ": current_is_part = True")
            next_to_part[char] = True
            if char >0:
                next_to_part[char-1] = True
            if char < len(current_line):
                next_to_part[char+1] = True
        if next_line[char] in symbols:
            print("Symbol on next line at character " + str(char) + ": current_is_part = True")
            next_to_part[char] = True
            if char >0:
                next_to_part[char-1] = True
            if char < len(current_line):
                next_to_part[char+1] = True

    is_part_number = False*len(current_line)
    numbers_count = 0

    for char in range(len(current_line)):
        if next_to_part[char]:
            is_part_number[char] = True
            i = 0
            while next_to_part[char+i].isnumeric():
                is_part_number[char+i] = True
                i+=1
        if current_line[char].isnumeric():
            numbers_count += 1
        if current_line[char]=='.' or char == len(current_line):
            for i in range(numbers_count):
                current_line[char-i] = True
    
    print("end of line")
    if current_number != '':
        subtotal += int(current_number)

        # this code should scan the current line for symbols, and set the relevant items in a list of booleans to True
        # it then should read the numbers on a line sequentially, adding to the line subtotal if each number overlaps with a symbol
        # 

