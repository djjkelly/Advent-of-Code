#!/usr/bin/env python3
#https://adventofcode.com/2023/day/3

try:
    with open("2023/2023_Day3_input.txt") as file_object:
        file_content = file_object.readlines()
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"An error was encountered: {e}")

symbols = "*" #"!@£$%^&*()-=_+|/\\#"

total = 0

for line_number in range(len(file_content)):
    subtotal = 0
    
    current_line = file_content[line_number].strip()
    if line_number < len(file_content)-1:
        next_line = file_content[line_number + 1].strip()
    else:
        next_line = ''
        for character in current_line:
            next_line += '.'
    if line_number == 0:
        previous_line = ''
        for character in current_line:
            previous_line += '.'

    previous_line = '.12..'
    current_line =  '...*.'
    next_line =     '.21..'

    print(previous_line)
    print(current_line)
    print(next_line)
    
    previous_working_number = ''
    current_working_number = ''
    next_working_number = ''

    for index,character in enumerate(current_line):
        parts_found = 0
        character_is_symbol = False
        up_left = False
        down_left = False
        up = False
        down = False
        is_gear = False
        print('moving to character number ' + str(index) + ": " + character)

        if character in symbols:
            print("* symbol found!")
            character_is_symbol = True
            if previous_working_number != '':
                parts_found += 1
                print("Nearby part found left and up")
                up_left = True
            if current_working_number != '':
                parts_found += 1
                print("Nearby part found left")
            if next_working_number != '':
                parts_found += 1
                print("Nearby part found left and down")
                down_left = True

        if previous_line[index].isnumeric():
            up = True
            previous_working_number += previous_line[index]
            print("Previous line working number updated: " + str(previous_working_number))
            if not up_left:
                parts_found += 1
                print("Part found directly up!")
        if character.isnumeric():
            current_working_number += character
            print("Current line working number updated: " + str(current_working_number))
        if next_line[index].isnumeric():
            down = True
            next_working_number += next_line[index]
            print("Next line working number updated: " + str(next_working_number))
            if not down_left:
                parts_found += 1
                print("Part found directly down!")

        if index < len(current_line)-1:
            if previous_line[index+1].isnumeric():
                if not up:
                    parts_found += 1
                    print("Part found diagonally up and right!")
            if current_line[index+1].isnumeric() and not character.isnumeric():
                    parts_found += 1
                    print("Part found to right!")
            if next_line[index+1].isnumeric():
                if not down:
                    parts_found += 1
                    print("Part found diagonally down and right!")
        else:
            print("End of line_number " + str(line_number) + '.')

        if character_is_symbol:
            print("Parts found for this symbol: " + str(parts_found))
            if parts_found == 2:
                print("This part is a gear!")
        
        if is_gear:
            pass


    # leave this intact!
    previous_line = current_line
    #print ("Subtotal for line " + str(line_number) + " is " + str(subtotal))
    total += subtotal

"""
Subtotals expected:
Line 1: 0
Line 2: 514 * 844
Line 3: 377 + 783 + 9 + 855 + 940 + 463 + 844 + 679 = 4950

"""
print(total)