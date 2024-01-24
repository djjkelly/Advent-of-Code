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
"""
Subtotals expected:
line_number 0: 0
line_number 1: 514 * 844  =  433816
line_number 2: 855 * 548  +  869 * 254  =  689266
line_number 3: 377 * 36  +  679 * 768  =  535044
line_number 4: 197 * 909  +  336 * 759  +  817 * 427  +  748 * 450  +  621 * 169  =  1224505
line_number 5: 882 * 368  +  88 * 555  +  135 * 971  =  504501
line_number 6: 441 * 760  =  335160
line_number 7: 776 * 425  +  217 * 45  +  674 * 917  =  957623
"""
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

    #previous_line = '.12...'
    #current_line =  '...*..'
    #next_line =     '....34'

    print(previous_line)
    print(current_line)
    print(next_line)
    previous_working_number = ''
    current_working_number = ''
    next_working_number = ''

    for index,character in enumerate(current_line):
        parts_found = 0
        factors = []
        character_is_symbol = False
        up_left = False
        left = False
        down_left = False
        up = False
        down = False
        up_right = False
        down_right = False
        right = False
        is_gear = False

        up_right_string = ''
        right_string = ''
        down_right_string = ''
        #print('moving to character number ' + str(index) + ": " + character)

        if character in symbols:
            print("* symbol found!")
            character_is_symbol = True
            if previous_working_number != '':
                parts_found += 1
                up_left = True
                #print("Nearby part found left and up")
            if current_working_number != '':
                parts_found += 1
                left = True
                #print("Nearby part found left")
            if next_working_number != '':
                parts_found += 1
                down_left = True
                #print("Nearby part found left and down")

        if previous_line[index].isnumeric():
            up = True
            previous_working_number += previous_line[index]
            #print("Previous line working number updated: " + str(previous_working_number))
            if not up_left:
                parts_found += 1
        if character.isnumeric():
            current_working_number += character
            #print("Current line working number updated: " + str(current_working_number))
        if next_line[index].isnumeric():
            down = True
            next_working_number += next_line[index]
            #print("Next line working number updated: " + str(next_working_number))
            if not down_left:
                parts_found += 1

        if index < len(current_line)-1:
            if previous_line[index+1].isnumeric():
                up_right = True
                if not up:
                    parts_found += 1
                    #print("Part found diagonally up and right!")
            if current_line[index+1].isnumeric():
                    right = True
                    if not character.isnumeric():
                        parts_found += 1
                    #print("Part found to right!")
            if next_line[index+1].isnumeric():
                down_right = True
                if not down:
                    parts_found += 1
                    #print("Part found diagonally down and right!")
        else:
            print("Last character of line_number " + str(line_number) + '.')

        if character_is_symbol:
            print("Parts found for this symbol: " + str(parts_found))
            if parts_found == 2:
                is_gear = True

        if is_gear:
            print("This part is a gear!")
            print(next_working_number)
            if up_left and not up:
                factors.append(previous_working_number)
            if left:
                factors.append(current_working_number)
            if down_left and not down:
                factors.append(next_working_number)

            if up_left and up and not up_right:
                factors.append(previous_working_number)
            if down_left and down and not down_right:
                factors.append(next_working_number)


            if up and not up_left and not up_right:
                    factors.append(previous_working_number)
            if down and not down_left and not down_right:
                    factors.append(next_working_number)

            if up_right:
                if not up:
                    previous_working_number = ''
                count = 1
                while index + count < len(current_line) and previous_line[index + count].isnumeric():
                    previous_working_number += previous_line[index+count]
                    count +=1
                factors.append(previous_working_number)
            if down_right:
                if not down:
                    next_working_number = ''
                count = 1
                while index + count < len(current_line) and next_line[index + count].isnumeric():
                    next_working_number += next_line[index+count]
                    count +=1
                factors.append(next_working_number)
            if right:
                count = 1
                while index + count < len(current_line) and current_line[index + count].isnumeric():
                    right_string += current_line[index + count]
                    count +=1
                factors.append(right_string)

            print(f"The factors are: {factors}")
            subtotal += int(factors[0])*int(factors[1])

        if previous_line[index] == '.':
            previous_working_number = ''
        if character == ".":
            current_working_number = ''
        if next_line[index] == '.':
            next_working_number = ''
    print(f"Subtotal is {subtotal}")
    
    previous_line = current_line
    #print ("Subtotal for line " + str(line_number) + " is " + str(subtotal))
    total += subtotal
print(total)