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

for line_number in range(len(file_content)):

    current_line = file_content[line_number].strip()
    try:
        next_line = file_content[line_number + 1].strip()
    except:
        next_line = ''
        for character in range(len(current_line)):
            next_line.append('.')

    current_line = '...234...'
    next_line    = '..!......'

    line_total = 0

    current_line_num = ''
    next_line_num = ''
    diagonal_down = '' # This is any numbers on the next_line affected by symbols on the current_line
    diagonal_up = '' # This is any numbers on the current_line affected by symbols on the next_line

    current_is_part = False
    next_is_part = False

    for char in range(len(current_line)):
        if current_line[char].isnumeric():
            current_line_num += current_line[char]
            #print("current_line_num is " + current_line_num)

        if next_line[char].isnumeric():
            next_line_num += next_line[char]
            #print("next_line_num is " + next_line_num)
        
        # diagonal down and to right
        if current_line[char] in symbols:
            print("Symbol on current line: current_is_part = True")
            current_is_part = True
            i = 1
            while next_line[char+i].isnumeric():
                diagonal_down += next_line[char+i]
                i += 1
            print("Number found down and right from current line symbol, added to diagonal_down: " + diagonal_down)
        
        # diagonal up and to right
        if next_line[char] in symbols:
            print("Symbol on next line: next_is_part = True")
            next_is_part = True
            i = 1
            while current_line[char+i].isnumeric():
                diagonal_up += current_line[char+i]
                i += 1
            print("Number found up and right from next line symbol, added to diagonal_up: " + diagonal_up)

        # This takes the num being stored for the CURRENT line and adds it to the line total
        if current_line[char] == '.' or char == len(current_line):
            if current_is_part and current_line_num != '':
                print("Eligible number ended: Line total updated with current_line_num; current_line_num set to False")
                line_total += current_line_num
                current_is_part = False
    print("End of the line!")

    
        
        
        
        # if there is a number:
            # get the whole number (go until a dot or the end of the line)
            # scan for symbols (right, down, diagonal)
        
        # if there is a symbol:
            # scan for numbers
            # get the whole number (go until a dot or the end of the line)
        #
        #
        #
