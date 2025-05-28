#!/usr/bin/env python3
#https://adventofcode.com/2024/day/4

folder = '2024/'
filename = '2024_Day4_input'
extension = '.txt'
full_path = folder + filename + extension
with open(full_path,'r') as file_object:
    file_content = file_object.readlines()

rows = len(file_content)

list_of_lists = [['' for x in range(rows)]for y in range(rows)]
total = 0

for i,line in enumerate(file_content):
    line = line.strip()
    for j,char in enumerate(line):
        list_of_lists[i][j] = char

directions = {'down_right':(1,1),'up_right':(-1,1),'down_left':(1,-1),'up_left':(-1,-1)}
keyword = 'MAS'

def is_x_mas(i,j):
    if list_of_lists[i+1][j+1] == 'M' and list_of_lists[i-1][j-1] == 'S':
        if list_of_lists[i+1][j-1] == 'M' and list_of_lists[i-1][j+1] == 'S':
            print('Match found at ('+str(i)+','+str(j)+')!')
            return True
    if list_of_lists[i+1][j+1] == 'M' and list_of_lists[i-1][j-1] == 'S':
        if list_of_lists[i-1][j+1] == 'M' and list_of_lists[i+1][j-1] == 'S':
            print('Match found at ('+str(i)+','+str(j)+')!')
            return True
    if list_of_lists[i-1][j-1] == 'M' and list_of_lists[i+1][j+1] == 'S':
        if list_of_lists[i+1][j-1] == 'M' and list_of_lists[i-1][j+1] == 'S':
            print('Match found at ('+str(i)+','+str(j)+')!')
            return True
    if list_of_lists[i-1][j-1] == 'M' and list_of_lists[i+1][j+1] == 'S':
        if list_of_lists[i-1][j+1] == 'M' and list_of_lists[i+1][j-1] == 'S':
            print('Match found at ('+str(i)+','+str(j)+')!')
            return True

for i,line in enumerate(list_of_lists):
    for j,char in enumerate(line):
        if char == keyword[1]:
            if i > 0 and j > 0 and i < rows-1 and j < rows-1:
                if is_x_mas(i,j):
                    total += 1
                    print('Matches: '+ str(total))
print(total)

test_dictionary = {
    '2024_Day4_input':
    {'attempts':(None,),
    'low':None,'high':None,'answer':1822},

    '2024_Day4_testinput':
    {'answer':9},
}

from testmodule import test_function
test_function(test_dictionary,filename,total)
'''

'''