#!/usr/bin/env python3
#https://adventofcode.com/2023/day/14

folder = '2023/'
filename = '2023_Day14_input'
extension = '.txt'
full_path = folder + filename + extension

with open(full_path,'r') as file_object:
    file_content = file_object.readlines()
content_list = []
for line in file_content:
    line = line.strip()
    new_line = []
    for char in line:
        new_line.append(char)
    content_list.append(new_line)

def slide_Os(input_content):
    length = len(input_content[0])
    drop_points = [0] * length
    for line_no,line in enumerate(input_content):
        '''print(drop_points)
        for l in input_content:
            print(l)'''
        for char_no,char in enumerate(line):
            if char == '#':
                drop_points[char_no] = line_no + 1
            if char == 'O':
                if drop_points[char_no] < line_no:
                    input_content[line_no][char_no] = '.'
                    input_content[drop_points[char_no]][char_no] = 'O'
                drop_points[char_no] += 1
    return input_content
#print(f'test for slide_0s {slide_Os(content_list)}')
processed_content = slide_Os(content_list)

#interim_test_content = ['OOOO.#.O..','OO..#....#','OO..O##..O','O..#.OO...','........#.','..#....#.#','..O..#.O.O','..O.......','#....###..','#....#....']
def count_total(list_of_strings):
    total = 0
    length = len(list_of_strings)
    for line_no,line in enumerate(list_of_strings):
        for char in line:
            if char == 'O':
                total += (length - line_no)
    return total
total = count_total(processed_content)
print(f'test of count_total. Should be 136 for test content : {total}')

'''
testinput should have a total load of 136
Correct answer obtained = 112773
'''
test_dictionary = {
    '2023_Day14_input':
    {'answer':112773},
}

from testmodule import test_function
test_function(test_dictionary,filename,total)