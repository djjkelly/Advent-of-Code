#!/usr/bin/env python3
#https://adventofcode.com/2023/day/25

from random import randint, choice

folder = '2023/'
filename = '2023_Day25_testinput'
extension = '.txt'
full_path = folder + filename + extension
with open(full_path,'r') as file_object:
    file_content = file_object.readlines()
total = 0

def consistent_split(string):
    if len(string.split()) == 1:
        return [string.strip()]
    else:
        return string.split()

connections = {}
input_dict = {}
components_list = []
for line in file_content:
    line = line.strip()
    component_name = line.split(':')[0]
    linked_components = line.split(':')[1]
    linked_components = consistent_split(linked_components)
    input_dict[component_name] = linked_components
    #print('component_name',component_name)
    #print('linked_components', linked_components)
    if component_name in connections:
        connections[component_name].extend(linked_components)
    else:
        connections[component_name] = linked_components
    for linked_component_name in linked_components:
        if linked_component_name in connections:
            connections[linked_component_name].append(component_name)
        else:
            connections[linked_component_name] = [component_name]

        if component_name not in components_list:
            components_list.append(component_name)
        if linked_component_name not in components_list:
            components_list.append(linked_component_name)
components_list_length = len(components_list)
print('length of components list: ', components_list_length)

for index,component_name in enumerate(components_list):
    count = len(connections[component_name])
    components_list[index] = (component_name,count)
components_list = sorted(components_list, key=lambda x: x[1], reverse=True)
'''
There are 15 components in the test data. Number of wires is 105
There are 1458 components in the real data. Number of possible wires is 1062153 (1,062,153)
'''
wires_list = []
for index, (component_1,count1) in enumerate(components_list):
    for index, (component_2,count2) in enumerate(components_list[index + 1:]):
        if component_2 in connections[component_1] or component_1 in connections[component_2]:
            wires_list.append(([component_1, component_2],count1 + count2))
wires_list_length = len(wires_list)
print('length of wires list: ', wires_list_length)
wires_list = sorted(wires_list, key=lambda x: x[1], reverse=True)

wires_list = [tuple(sublist[0]) for sublist in wires_list]

# connections = {}, input_dict = {}, components_list = []
# this version considers wires rather than individual components
def test_probe_wire(cycle_number,removed_wires):
    frequency_analysis = {}
    wire_name = wires_list[1] # this is an arbitrary starting point
    for i in range(cycle_number):
        component_name_0 = wire_name[0]
        component_name_1 = wire_name[1]
        # add component count in frequency analysis
        if wire_name in frequency_analysis:
            frequency_analysis[wire_name] += 1
        elif (wire_name[1],wire_name[0]) in frequency_analysis:
            frequency_analysis[wire_name[1],wire_name[0]] += 1
        else:
            frequency_analysis[wire_name] = 1
        valid_selection = False
        component_name_0 = component_name_1
        while not valid_selection:
            component_name_1 = choice(connections[component_name_0])
            if (component_name_0,component_name_1) not in removed_wires and (component_name_1,component_name_0) not in removed_wires:
                valid_selection = True
        wire_name = (component_name_0,component_name_1)
    return frequency_analysis
cycle_number = 1000000
removed_wires = ((None,None),(None,None),(None,None))
frequency_analysis = test_probe_wire(cycle_number,removed_wires)
len_frequency_analysis = len(frequency_analysis)
print(len_frequency_analysis)

def is_network_split(removed_wires):
    test_cycles = 10000
    test_dictionary = test_probe_wire(test_cycles,removed_wires)
    for wire in wires_list:
        if wire not in test_dictionary and (wire[1],wire[0]) not in test_dictionary and wire not in removed_wires:
            return True
    return False
removed_wires = (('hfx','pzl'),('bvb','cmg'),('nvd','jqt'))
#print(is_network_split(removed_wires))

def incremental_combinations(data):
    n = len(data)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                yield (data[i], data[j], data[k])

# need to find "THE" 3 wires which can be disconnected to separate the components into 2 separate groups
def solve():
    generator = incremental_combinations(wires_list)
    count = 0
    for combination in generator:
        count += 1
        answer_found = is_network_split(combination)
        if answer_found:
            print('Answer found!: ',combination)
            print(count) # should be less than 35937 which is the number of combinations for testinput
    answer = 1
    return answer

total = solve()
print('total:',total)
test_dictionary = {
    '2023_Day25_input':
    {'attempts':(None),
    'low':None,'high':None,'answer':None},
    '2023_Day25_testinput':
    {'answer':54},
}

from testmodule import test_function
test_function(test_dictionary,filename,total)
'''


'''