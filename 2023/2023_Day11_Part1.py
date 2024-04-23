#!/usr/bin/env python3
#https://adventofcode.com/2023/day/11

with open("2023/2023_Day11_input.txt") as file_object:
    file_content = file_object.readlines()

array = []
count = 0
galaxy_char_numbers = []
for line_num,line in enumerate(file_content):
    line = line.strip()
    new_line = []
    for char_num,char in enumerate(line):
        if char == '#':
            galaxy_char_numbers.append(char_num)
            count += 1
            char = count
        new_line.append(char)
    array.append(new_line)
    if all(x == '.' for x in line):
        array.append(new_line)

def insert_column(position):
    for line_number,line in enumerate(array):
        new_line = []
        for char_num,char in enumerate(line):
            if char_num == position:
                new_line.append('.')
            new_line.append(char)
        array[line_number] = new_line
    return array

missing_columns = []
for column_no in range(char_num+1):
    if column_no not in galaxy_char_numbers:
        print('column_no not found', column_no)
        missing_columns.append(column_no)

i = 0
for column_no in missing_columns:
    array = insert_column(column_no+i)
    i += 1

print('array below:')
for line in array:
    print(''.join(str(x) for x in line))

galaxy_char_numbers = list(set(galaxy_char_numbers))
print(galaxy_char_numbers)

pos_dict = {}
for line_num,line in enumerate(array):
    for char_num,char in enumerate(line):
        if type(char) is int:
            pos_dict[char] = [line_num,char_num]
print(pos_dict)

total_length = 0
for count1 in range(1,count+1):
    for count2 in range(count1,count+1):
        if count2 == count1:
            continue
        print('count1: ',count1,'count2: ',count2)
        x1,y1,x2,y2 = pos_dict[count1][1],pos_dict[count1][0],pos_dict[count2][1],pos_dict[count2][0]
        diff_x,diff_y = abs(x1 - x2),abs(y1 - y2)
        length = diff_x + diff_y
        print(length)
        total_length += length
print(total_length)
'''

'''
