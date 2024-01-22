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
previous_line = '............................................................................................................................................'
'''Each symbol is surrounded by an imaginary "square" of eligibility.
Within this square every digit found will be considered as an eligible digit in a part number.
All digits sequentially adjacent to a digit in a part number eligible digit is included in the part number.
'''
total = 0
for line_number, current_line in enumerate(file_content):
    current_line = current_line.strip()

    # previous_line = '.....654.'
    # current_line = '855*.....'

    print(previous_line)
    print(current_line)

    subtotal = 0

    current_number_string = '0'
    previous_line_number_string = '0'
    current_number_is_part_number = False
    number_above_is_part_number = False
    for character_number,character in enumerate(current_line):
        character_above = previous_line[character_number]
        # this section sets "is_part_number" to True if any of the relevant 2 or 3 characters on the line above are symbols.
        if previous_line[character_number] in symbols:
            current_number_is_part_number = True
            number_above_is_part_number = True

        if character_number > 0 and previous_line[character_number-1] in symbols:
            current_number_is_part_number = True
            number_above_is_part_number = True

        if character_number+1 < len(current_line):
            if previous_line[character_number+1] in symbols:
                current_number_is_part_number = True
            number_above_is_part_number = True

        # this section looks for numbers on the line above which may correspond to a symbol on the current line
        if previous_line[character_number].isnumeric():
            previous_line_number_string += previous_line[character_number]
            print("Number found on previous line! Previous number updated to " + previous_line_number_string)
        else:
            previous_line_number_string = '0'

        if character == "." or character_number==len(current_line)-1:
            if current_number_is_part_number and current_number_string != '0':
                print("Current number found. Adding " + current_number_string)
                subtotal += int(current_number_string)
            current_number_is_part_number = False
            number_above_is_part_number = False # sceptical of this

            current_number_string = '0'

            if number_above_is_part_number:
                if previous_line[character_number+1].isnumeric():
                    previous_line_number_string += previous_line[character_number+1]
                    if previous_line[character_number+2].isnumeric():
                        previous_line_number_string += previous_line[character_number+2]

                print("Number above found. Adding " + previous_line_number_string)
                subtotal += int(previous_line_number_string)
                number_above_is_part_number = False
                previous_line_number_string = '0'
    
        elif character.isnumeric():
            current_number_string+=character
            print("Number found! Number updated to " + current_number_string)
        elif character in symbols:
            current_number_is_part_number = True
            number_above_is_part_number = True
        else:
            print("ERROR: Something has gone wrong, character unaccounted for!")
    if current_number_is_part_number:
        print("Adding " + current_number_string)
        subtotal += int(current_number_string)

    # This line will need to be at the end of the character-wise for loop.
    previous_line = current_line


print("Total: " + str(total))

'''
Line 1 ("0") should have a total of 0
Line 2 should add a total of ^0^ + 305 + 901 + 514 = 1720
Line 3 should have a total of ^1720^ + 783 + 9 + 855 + 940 + 844 + 257 = 5408
'''

# remember to deal with the case where a number on the line above has already been counted.