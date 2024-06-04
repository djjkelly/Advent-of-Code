#!/usr/bin/env python3
#https://adventofcode.com/2023/day/20

folder = '2023/'
filename = '2023_Day20_input'
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
        modules[module_name] = {'type':module_type,'destinations':destinations,'memory':dict({})}
for module_name,module_info in modules.items():
    if module_info['type'] == 'conjunction':
        connected_inputs = {source_name: 'low' for source_name, source_info in modules.items() if module_name in source_info.get('destinations', [])}
        module_info['memory'] = connected_inputs
    print(f'{module_name},{module_info}')

def send_pulses(modules,button_pushes):
    total_low = 0
    total_high = 0
    for push in range(1,button_pushes+1):
        pulse = 'low'
        current_modules = modules['broadcaster']['destinations']
        current_status = [(item,pulse) for item in current_modules]
        next_status = []
        print('\nnew push! starts off with button to broadcast, low pulses: 1')
        high_pulse_count = sum(item.count('high') for item in current_status)
        low_pulse_count = sum(item.count('low') for item in current_status) + 1
        print(f'broadcasting to {current_modules}! high pulses: {high_pulse_count}, low pulses: {low_pulse_count}')

        while current_status != []: # continues while signals being sent
            for current_module,pulse in current_status: # this iterates through an entire batch of commands before moving onto the next
                if current_module not in modules:
                    continue
                next_modules = modules[current_module]['destinations']
                if modules[current_module]['type'] == 'flip-flop':
                    print(f'flip-flop module: {current_module}')
                    if pulse == 'high':
                        next_pulse = None
                        print(f'current module {current_module} receives high pulse - ignoring!')
                    elif pulse == 'low':
                        if modules[current_module]['state'] == 'off':
                            modules[current_module]['state'] = 'on'
                            next_pulse = 'high'
                            high_pulse_count += len(next_modules)
                            print(f'current module \'{current_module}\' receives low pulse, switches on and sends a high pulse to {next_modules}')
                        elif modules[current_module]['state'] == 'on':
                            modules[current_module]['state'] = 'off'
                            next_pulse = 'low'
                            low_pulse_count += len(next_modules)
                            print(f'current module \'{current_module}\' receives low pulse, switches off and sends a low pulse to {next_modules}')
                elif modules[current_module]['type'] == 'conjunction':
                    print(f'conjunction module: {current_module}')
                    if all(value == 'high' for value in modules[current_module]['memory'].values()):
                        next_pulse = 'low'
                        low_pulse_count += len(next_modules)
                        print(f'sent \'{next_pulse}\' to {modules[current_module]['destinations']}')
                    else:
                        print(f'not all memory high - \'{current_module}\' sends high pulse to {modules[current_module]['destinations']}')
                        next_pulse = 'high'
                        high_pulse_count += len(next_modules)
                for next_module_name in modules[current_module]['destinations']:
                    if next_module_name in modules:
                        if modules[next_module_name]['type'] == 'conjunction':
                            if current_module in modules[next_module_name]['memory']:
                                if next_pulse != None:
                                    modules[next_module_name]['memory'][current_module] = next_pulse
                if next_pulse != None:
                    next_status.extend([(item,next_pulse) for item in next_modules])
            print(f'for loop complete! high pulses: {high_pulse_count}, low pulses: {low_pulse_count}')
            print('batch of signals complete! next status:',next_status)
            current_status = next_status
            next_status = []
        total_low += low_pulse_count
        total_high += high_pulse_count
    print('total_low:',total_low,'total_high:',total_high)
    total = total_low * total_high
    return total

button_pushes = 1000
total = send_pulses(modules,button_pushes)
print('total:',total)
test_dictionary = {
    '2023_Day20_input':
    {'attempts':(None),
    'low':None,'high':None,'answer':731517480},
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