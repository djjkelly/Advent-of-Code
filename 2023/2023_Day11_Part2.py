#!/usr/bin/env python3
#https://adventofcode.com/2023/day/11

folder = '2023/'
filename = '2023_Day11_input'
extension = '.txt'
full_path = folder + filename + extension

with open(full_path) as file_object:
    file_content = file_object.readlines()

def calculate_total_length(file_content):
    array = []
    count = 0
    galaxy_line_numbers = []
    galaxy_char_numbers = []
    for line_num,line in enumerate(file_content):
        line = line.strip()
        new_line = []
        for char_num,char in enumerate(line):
            if char == '#':
                galaxy_char_numbers.append(char_num)
                galaxy_line_numbers.append(line_num)
                count += 1
                char = count
            new_line.append(char)
        array.append(new_line)

    missing_columns = []
    for column_num in range(char_num+1):
        if column_num not in galaxy_char_numbers:
            print('column_num not found', column_num)
            missing_columns.append(column_num)
    print('missing columns: ',missing_columns)

    missing_lines = []
    for row_num in range(line_num+1):
        if row_num not in galaxy_line_numbers:
            print('row_num not found',row_num)
            missing_lines.append(row_num)
    #print('missing lines: ',missing_lines)

    pos_dict = {}
    for line_num,line in enumerate(array):
        for char_num,char in enumerate(line):
            if type(char) is int:
                pos_dict[char] = [line_num,char_num]
    print(pos_dict)

    expansion_coefficient = 1000000

    total_length = 0
    for count1 in range(1,count+1):
        for count2 in range(count1,count+1):
            length = 0
            if count2 == count1:
                continue
            x1,y1,x2,y2 = pos_dict[count1][1],pos_dict[count1][0],pos_dict[count2][1],pos_dict[count2][0]
            
            for n in range(min(x1,x2),max(x1,x2)):
                if n in missing_columns:
                    length += (expansion_coefficient-1)
            for n in range(min(y1,y2),max(y1,y2)):
                if n in missing_lines:
                    length += (expansion_coefficient-1)

            length += abs(x1 - x2) + abs(y1 - y2)
            #print('count1: ',count1,'count2: ',count2,'length:',length)
            total_length += length
    print('total_length: ',total_length)
    return total_length
total_length = calculate_total_length(file_content)
'''
test should be 1030 for an expansion factor of 10 (currently 1112 - 82 off)
test should be 8410 for an expansion factor of 100 (currently 8492 - 82 off)
'''
test_dictionary = {
    '2023_Day11_input':
    {'answer':707505470642},
}

from testmodule import test_function
test_function(test_dictionary,filename,total_length)