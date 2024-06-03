#!/usr/bin/env python3
#https://adventofcode.com/2023/day/21

folder = '2023/'
filename = '2023_Day20_test1_input'
extension = '.txt'
full_path = folder + filename + extension
total = 0
with open(full_path,'r') as file_object:
    file_content = file_object.readlines()

modules = {}

def consistent_split(string,delimiter):
    if delimiter in string:
        return string.split(delimiter)
    else:
        return [string]

for line_no,line in enumerate(file_content):
    split_line = line.strip().split(' -> ')
    if split_line[0] == r'broadcaster':
        destinations = consistent_split(split_line[1],', ')
        modules['broadcaster'] = {'type':'broadcaster','destinations':destinations}
    elif split_line[0][0] == r'%':
        module_type = r'flip-flop'
        module_name = split_line[0][1:]
        destinations = consistent_split(split_line[1],', ')
        modules[module_name] = {'type':module_type,'destinations':destinations,'state':'off'}
    elif split_line[0][0] == r'&':
        module_type = r'conjunction'
        module_name = split_line[0][1:]
        destinations = consistent_split(split_line[1],', ')
        modules[module_name] = {'type':module_type,'destinations':destinations,'memory':['low']}
for item in modules.items():
    print(item)

def send_pulses(modules,button_pushes):
    total_low = 0
    total_high = 0
    for push in range(1,button_pushes+1):
        pulse = 'low'
        current_modules = modules['broadcaster']['destinations']
        current_status = [(item,pulse) for item in current_modules]
        next_status = []
        print('\nnew push!\n')
        high_pulse_count = sum(item.count('high') for item in current_status)
        low_pulse_count = sum(item.count('low') for item in current_status)
        while current_status != []:
            for current_module,pulse in current_status: # this iterates through an entire batch of commands before moving onto the next
                    next_modules = modules[current_module]['destinations']
                    if modules[current_module]['type'] == 'flip-flop':
                        print('flip-flop')
                        if pulse == 'high':
                            next_pulse = None
                            print(f'current module {current_module} receives high pulse - ignoring!')
                        elif pulse == 'low':
                            if modules[current_module]['state'] == 'off':
                                modules[current_module]['state'] = 'on'
                                next_pulse = 'high'
                                high_pulse_count += 1
                                print(f'current module {current_module} receives low pulse, switches on and produces a high pulse')
                            elif modules[current_module]['state'] == 'on':
                                modules[current_module]['state'] = 'off'
                                next_pulse = 'low'
                                low_pulse_count += 1
                                print(f'current module {current_module} receives low pulse, switches off and produces a low pulse')
                    elif modules[current_module]['type'] == 'conjunction':
                        if pulse == 'low':
                            print(f'current module {current_module} receives low pulse, conjunction memory updated to low')
                            modules[current_module]['memory'] = 'low'
                        elif pulse == 'high':
                            print(f'current module {current_module} receives high pulse, conjunction memory updated to high')
                            modules[current_module]['memory'] = 'high'
                        memory = modules[current_module]['memory']
                        if memory == 'high':
                            print('all memory high - sending low pulse')
                            next_pulse = 'low'
                            low_pulse_count += 1
                        else:
                            print('not all memory high - sending high pulse')
                            next_pulse = 'high'
                            high_pulse_count += 1
                    if pulse != None:
                        next_status.extend([(item,next_pulse) for item in next_modules])
                    print(f'for loop complete! high pulses: {high_pulse_count}, low pulses: {low_pulse_count}')
            current_status = next_status
            next_status = []
        total_low += low_pulse_count
        total_high += high_pulse_count
    total = total_low * total_high
    return total

button_pushes = 1000
total = send_pulses(modules,button_pushes)
print('total:',total)
test_dictionary = {
    '2023_Day20_input':
    {'attempts':(None),
    'low':None,'high':None,'answer':None},
    '2023_Day20_test1_input':
    {'attempts':(None),
    'answer':32000000},
    '2023_Day20_test2_input':
    {'attempts':(None),
    'answer':11687500},
}

from testmodule import test_function
test_function(test_dictionary,filename,total)
'''

'''