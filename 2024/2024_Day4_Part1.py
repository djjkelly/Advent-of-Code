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

directions = {'down':(1,0),'right':(0,1),'up':(-1,0),'left':(0,-1),'down_right':(1,1),'up_right':(-1,1),'down_left':(1,-1),'up_left':(-1,-1)}
keyword = 'XMAS'
kw_len = len(keyword)-1

def is_direction_xmas(i,j,direction):
    (d_i,d_j) = directions[direction]
    if i + d_i * (kw_len) < 0 or j + d_j * (kw_len) < 0 or (i + d_i * kw_len) >= rows or (j + d_j * kw_len) >= rows:
        #print('Not long enough to '+ direction +'! Returning false')
        return False
    else:
        for char_no,char in enumerate(keyword):
            if char != list_of_lists[i + char_no*d_i][j + char_no*d_j]:
                #print('Match not found ' + direction + ', returning False')
                return False
        print('Match found at ('+str(i)+','+str(j)+')! towards '+ direction)
        return True

for i,line in enumerate(list_of_lists):
    for j,char in enumerate(line):
        if char == keyword[0]:
            for direction in directions.keys():
                if is_direction_xmas(i,j,direction):
                    total += 1
                    print('Matches: '+ str(total))

print(total)

test_dictionary = {
    '2024_Day4_input':
    {'attempts':(None,),
    'low':2380,'high':None,'answer':2401},

    '2024_Day4_testinput':
    {'answer':18},
}

from testmodule import test_function
test_function(test_dictionary,filename,total)
'''

'''