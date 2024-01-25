#!/usr/bin/env python3
#https://adventofcode.com/2023/day/3
total = 0
try:
    with open("2023/2023_Day3_input.txt") as file_object:
        file_content = file_object.readlines()
    symbols = "*"
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
    correct total: 81997870
    """
    for line_number in range(len(file_content)):
        subtotal = 0
        
        line = file_content[line_number].strip()
        if line_number < len(file_content)-1:
            line_below = file_content[line_number + 1].strip()
        else:
            line_below = ''
            for character in line:
                line_below += '.'
        if line_number == 0:
            line_above = ''
            for character in line:
                line_above += '.'

        print(f"{line_above}\n{line}\n{line_below}")

        working_number_above = ''
        working_number = ''
        working_number_below = ''

        for index,character in enumerate(line):
            up_left = False
            left = False
            down_left = False
            up = False
            down = False
            up_right = False
            down_right = False
            right = False
            parts_found = 0
            factors = []
            is_gear = False

            if character in symbols:
                print("* symbol found!")
                if working_number_above!= '':
                    parts_found += 1
                    up_left = True
                    #print("Nearby part found left and up")
                if working_number != '':
                    parts_found += 1
                    left = True
                    #print("Nearby part found left")
                if working_number_below != '':
                    parts_found += 1
                    down_left = True
                    #print("Nearby part found left and down")
            if line_above[index].isnumeric():
                up = True
                working_number_above += line_above[index]
                #print("Previous line working number updated: " + str(previous_working_number))
                if not up_left:
                    parts_found += 1
            if character.isnumeric():
                working_number += character
                #print("Current line working number updated: " + str(current_working_number))
            if line_below[index].isnumeric():
                down = True
                working_number_below += line_below[index]
                #print("Next line working number updated: " + str(next_working_number))
                if not down_left:
                    parts_found += 1
            if index < len(line)-1:
                if line_above[index+1].isnumeric():
                    up_right = True
                    if not up:
                        parts_found += 1
                        #print("Part found diagonally up and right!")
                if line[index+1].isnumeric():
                        right = True
                        if not character.isnumeric():
                            parts_found += 1
                        #print("Part found to right!")
                if line_below[index+1].isnumeric():
                    down_right = True
                    if not down:
                        parts_found += 1
                        #print("Part found diagonally down and right!")

            if character in symbols:
                #print("Parts found for this symbol: " + str(parts_found))
                if parts_found == 2:
                    is_gear = True

            if is_gear:
                print(f"This part at character {index} of line {line_number} is a gear!")
                if up_left:
                    if not up:
                        factors.append(working_number_above)
                    if up and not up_right:
                        factors.append(working_number_above)
                if down_left:
                    if not down:
                        factors.append(working_number_below)
                    if down and not down_right:
                        factors.append(working_number_below)
                if left:
                    factors.append(working_number)
                if right:
                    working_number = ''
                    count = 1
                    while index + count < len(line) and line[index + count].isnumeric():
                        working_number += line[index + count]
                        count +=1
                    factors.append(working_number)
                if up and not up_left and not up_right:
                        factors.append(working_number_above)
                if down and not down_left and not down_right:
                        factors.append(working_number_below)
                if up_right:
                    if not up:
                        working_number_above = ''
                    count = 1
                    while index + count < len(line) and line_above[index + count].isnumeric():
                        working_number_above += line_above[index+count]
                        count +=1
                    factors.append(working_number_above)
                if down_right:
                    if not down:
                        working_number_below = ''
                    count = 1
                    while index + count < len(line) and line_below[index + count].isnumeric():
                        working_number_below += line_below[index+count]
                        count +=1
                    factors.append(working_number_below)

                print(f"The factors are: {factors}")
                subtotal += int(factors[0])*int(factors[1])

            if line_above[index] == '.':
                working_number_above = ''
            if character == ".":
                working_number = ''
            if line_below[index] == '.':
                working_number_below = ''
        print(f"Subtotal for line {line_number} is {subtotal}")
        
        line_above = line
        total += subtotal
    print(total)

except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"An error was encountered: {e}")