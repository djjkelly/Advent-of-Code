#!/usr/bin/env python3
#https://adventofcode.com/2023/day/25

folder = '2023/'
filename = '2023_Day25_input'
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
    print('component_name',component_name)
    print('linked_components', linked_components)
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
print('length of components list: ', len(components_list))

'''
There are 15 components in the test data. Number of wires is 105
There are 1458 components in the real data. Number of wires is 1062153 (1,062,153)
'''
wires_list = []
for index,component_1 in enumerate(components_list):
    for index,component_2 in enumerate(components_list[index + 1:]):
        wires_list.append(component_1 + ' ' + component_2)
print('length of wires list: ', len(wires_list))

# need to find "THE" 3 wires which can be disconnected to separate the components into 2 separate groups
def solve():
    answer = 1
    return answer

total = solve()
print('total:',total)
test_dictionary = {
    '2023_Day25_input':
    {'attempts':(None),
    'low':None,'high':None,'answer':None},
    '2023_Day25_testinput':
    {'answer':None},
}

from testmodule import test_function
test_function(test_dictionary,filename,total)
'''


'''