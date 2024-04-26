#!/usr/bin/env python3
#https://adventofcode.com/2023/day/12

import math
from itertools import product
import cProfile

with open("2023/2023_Day12_input.txt") as file_object:
    file_content = file_object.readlines()

content_list = []
for line in file_content:
    line = line.strip()
    condition_records = line.split()[0]
    damaged_group_sizes = line.split()[1]
    damaged_group_sizes = damaged_group_sizes.split(',')
    content_list.append([condition_records,damaged_group_sizes])

def generate_combinations(uncertain_springs,number_expected):
    all_combinations = [''.join(seq) for seq in product('01',repeat=uncertain_springs)]
    relevant_combinations = []
    for string in all_combinations:
        if string.count('1') == number_expected:
            relevant_combinations.append(string)
    return relevant_combinations

def make_full_strings(condition_records,test_list):
    new_list = []
    for test_string in test_list:
        test_index = 0
        new_condition_records = condition_records
        for condition_index,character in enumerate(condition_records):
            if character == '?':
                new_condition_records = new_condition_records[:condition_index]+test_string[test_index] + new_condition_records[condition_index + 1:]
                #print(f'replacing character at {condition_index} with new character: {test_string[test_index]}')
                test_index += 1
        new_list.append(new_condition_records)
    return new_list

def count_possibilities(input_list,damaged_group_sizes):
    count = 0
    for string in input_list:
        group_sizes = []
        group_size = 0
        for character in string:
            if character == '#' or character == '1':
                group_size += 1
            if character == '.' or character == '0':
                if group_size > 0:
                    group_sizes.append(str(group_size))
                group_size = 0
        if group_size > 0:
            group_sizes.append(str(group_size))
        if group_sizes == damaged_group_sizes:
            count += 1
    return count

'''
Test input expectations:
Number of arrangements per line should be 1, 4, 1, 1, 4, 10
Total for all lines should be 21 arrangements (1 + 4 + 1 + 1 + 4 + 10)
'''
total_possibilities = 0
for line_no,line in enumerate(content_list):
    #line = content_list[848]
    print(f'\nStarting line {line_no+1}: {line}')
    condition_records, damaged_group_sizes = line[0],line[1]
    line_possibilities = 0
    operational_springs = 0
    uncertain_springs = 0
    damaged_springs_found = 0
    damaged_springs_total = 0
    for char_no,character in enumerate(condition_records):
        if character == '?':
            uncertain_springs += 1
        elif character == '.':
            operational_springs += 1
        elif character == '#':
            damaged_springs_found += 1
    total_springs = char_no + 1
    #print(f'total of {total_springs} springs. uncertain_springs: {uncertain_springs}.')
    for group in damaged_group_sizes:
        damaged_springs_total += int(group)
    springs_to_find = damaged_springs_total - damaged_springs_found
    #print(f'{damaged_springs_found} springs found out of a total of {damaged_springs_total} damaged springs. Remaining springs_to_find: {springs_to_find}')
    print(f'looking for damaged springs_to_find of {springs_to_find} amongst {uncertain_springs} uncertain_springs')
    #cProfile.run('generate_combinations(uncertain_springs,springs_to_find)')
    test_list = generate_combinations(uncertain_springs,springs_to_find)
    #print('combinations predicted:',math.comb(uncertain_springs,springs_to_find))
    #cProfile.run('make_full_strings(condition_records,test_list)')
    test_list = make_full_strings(condition_records,test_list)
    #cProfile.run('count_possibilities(test_list,damaged_group_sizes)')
    line_possibilities = count_possibilities(test_list,damaged_group_sizes)
    print(line_possibilities)
    total_possibilities += line_possibilities


print('\nTotal possibilities: ',total_possibilities)
'''
I need to exclude damaged groups which are directly next to each other.

Correct answer obtained - 7260

Line 849 takes the longest: Starting line 849: ['????????????#?#?????', ['1', '1', '8', '1', '1']]. Damaged springs_to_find of 10 amongst 18 uncertain_springs
On this line, I have assessed the time taken per function after setting line to file_content[848].
generate_combinations:
         262376 function calls (262359 primitive calls) in 0.277 seconds
remove_wrong_numbers:
         529060 function calls (523048 primitive calls) in 87.261 seconds        This function needs to be reviewed!
make_full_strings:
         44064 function calls (44032 primitive calls) in 0.506 seconds
count_possibilities:
         235136 function calls (235099 primitive calls) in 0.585 seconds

The way I'm whittling down the combinations needs to be more efficient.
it seems the 'queue', 'threading', and 'remove' processes are taking the longest.

More details below:
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.014    0.014 2023_Day12_Part1.py:23(remove_wrong_numbers)
        1    0.000    0.000    0.014    0.014 <string>:1(<module>)
      564    0.000    0.000    0.000    0.000 pydev_is_thread_alive.py:9(is_thread_alive)
      282    0.002    0.000    0.007    0.000 pydevd.py:1381(has_user_threads_alive)
      564    0.001    0.000    0.001    0.000 pydevd.py:1499(get_internal_queue)
      564    0.001    0.000    0.001    0.000 pydevd.py:1533(check_output_redirect)
      282    0.001    0.000    0.002    0.000 pydevd.py:1626(notify_thread_created)
      282    0.011    0.000    0.024    0.000 pydevd.py:1681(process_internal_commands)
      282    0.002    0.000    0.011    0.000 pydevd.py:250(can_exit)
      282    0.000    0.000    0.002    0.000 pydevd_comm.py:416(empty)
      282    0.000    0.000    0.000    0.000 pydevd_constants.py:606(get_current_thread_id)
      282    0.000    0.000    0.000    0.000 pydevd_constants.py:626(get_thread_id)
      282    0.000    0.000    0.000    0.000 pydevd_constants.py:660(__enter__)
      282    0.000    0.000    0.000    0.000 pydevd_constants.py:663(__exit__)
      282    0.000    0.000    0.000    0.000 pydevd_daemon_thread.py:32(py_db)
      282    0.002    0.000    0.005    0.000 pydevd_utils.py:133(get_non_pydevd_threads)
 1365/800    0.120    0.000  156.245    0.195 queue.py:154(get)
     2446    0.003    0.000    0.004    0.000 queue.py:209(_qsize)
      282    0.001    0.000    0.002    0.000 queue.py:97(empty)
      282    0.000    0.000    0.000    0.000 threading.py:1213(daemon)
      282    0.000    0.000    0.001    0.000 threading.py:1463(current_thread)
      564    0.004    0.000    0.005    0.000 threading.py:1513(enumerate)
     2210    0.002    0.000    0.003    0.000 threading.py:278(__enter__)
     2210    0.003    0.000    0.004    0.000 threading.py:281(__exit__)
     1364    0.001    0.000    0.001    0.000 threading.py:287(_release_save)
     1364    0.003    0.000    0.006    0.000 threading.py:290(_acquire_restore)
     1364    0.001    0.000    0.002    0.000 threading.py:293(_is_owned)
     1363    0.017    0.000   86.934    0.064 threading.py:302(wait)
      282    0.000    0.000    0.001    0.000 threading.py:606(clear)
      563    0.005    0.000   17.436    0.031 threading.py:616(wait)
     1364    0.002    0.000    0.002    0.000 {built-in method _thread.allocate_lock}
      282    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
      2/1    0.073    0.036    0.014    0.014 {built-in method builtins.exec}
     2820    0.001    0.000    0.001    0.000 {built-in method builtins.getattr}
      564    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
     2728    0.001    0.000    0.001    0.000 {built-in method builtins.len}
     2400    0.001    0.000    0.001    0.000 {built-in method time.monotonic}
     2210    0.001    0.000    0.001    0.000 {method '__enter__' of '_thread.lock' objects}
      564    0.000    0.000    0.000    0.000 {method '__exit__' of '_thread.RLock' objects}
     3338    0.002    0.000    0.002    0.000 {method '__exit__' of '_thread.lock' objects}
   5453/7    0.404    0.000    0.106    0.015 {method 'acquire' of '_thread.lock' objects}
     1364    0.001    0.000    0.001    0.000 {method 'append' of 'collections.deque' objects}
        1    0.002    0.002    0.002    0.002 {method 'copy' of 'list' objects}
   262144    0.165    0.000    0.165    0.000 {method 'count' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      282    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
     1364    0.001    0.000    0.001    0.000 {method 'release' of '_thread.lock' objects}
     1364    0.001    0.000    0.001    0.000 {method 'remove' of 'collections.deque' objects}
   218386   86.422    0.000   86.422    0.000 {method 'remove' of 'list' objects}
      564    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
     1128    0.001    0.000    0.001    0.000 {method 'values' of 'dict' objects}
'''