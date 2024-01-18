#!/usr/bin/env python3
#https://adventofcode.com/2023/day/3

try:
    with open("2023/2023_Day3_input.txt") as file_object:
        file_content = file_object.readlines()
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"An error was encountered: {e}")

symbols = "!@£$%^&*()-=_+|/\\#"
previous_line = '............................................................................................................................................'
previous_line_number_string = ''
'''Each symbol is surrounded by an imaginary "square" of eligibility.
Within this square every digit found will be considered as an eligible digit in a part number.
All digits sequentially adjacent to a digit in a part number eligible digit is included in the part number.
'''
total = 0
for line_number, current_line in enumerate(file_content):
    is_part_number = False
    current_number_string = '0'
    for character_number,character in enumerate(current_line.strip()):
        if character == ".":
            if is_part_number:
                total += int(current_number_string)
            is_part_number = False
            current_number_string = '0'
        elif character.isnumeric():
            current_number_string+=character
            print("Number found! Number updated to " + current_number_string)
        elif character in symbols:
            is_part_number = True
            print("Symbol found!")
        else:
            print("ERROR: Something has gone wrong, character unaccounted for!")

    print(current_line)
    # These need to be the lines at the end of the character-wise for loop.
    line_before_last = previous_line
    previous_line = current_line


print("Remember this is not the real total until the non-part numbers have been filtered out. Total: " + str(total))

'''
Line 1 ("0") should have a total of 0
Line 2 should add a total of 901
Line 3 should have a total of 901 + 783 + 855 = 2539
Line 4 ("3") should have a total of 2539 + 377 + 742 + 548 + 463 + 844 + 254 + 679 = 6446

In other words, it might work to look one line up for numbers, but not a line down.
Similarly, for numbers on current line, it makes sense to look up a line for a symbol, but not look down a line.
This could avoid double counting.
'''

# remember to deal with the case at the end of each line (with no '.' present)?