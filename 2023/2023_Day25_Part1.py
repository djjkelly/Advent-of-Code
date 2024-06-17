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
print('length of components list: ', len(components_list))

for index,component_name in enumerate(components_list):
    count = len(connections[component_name])
    components_list[index] = (component_name,count)
components_list = sorted(components_list, key=lambda x: x[1], reverse=True)
'''
There are 15 components in the test data. Number of wires is 105
There are 1458 components in the real data. Number of wires is 1062153 (1,062,153)
'''
wires_list = []
for index, (component_1,count1) in enumerate(components_list):
    for index, (component_2,count2) in enumerate(components_list[index + 1:]):
        wires_list.append(((component_1, component_2),count1 + count2))
wires_list_length = len(wires_list)
print('length of wires list: ', wires_list_length)
wires_list = sorted(wires_list, key=lambda x: x[1], reverse=True)

print_range = 10
for i in range(print_range):
    print(f'printing element {i} of wires_list: {wires_list[i]}.')

def generate_combinations(data):
    n = len(data) // 2 # if the calculation is taking too long we can maybe get away with shortening the list
    list = []
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                list.append((data[i], data[j], data[k]))
    return list
combination_list = generate_combinations(wires_list)
print('length of combinations list: ',len(combination_list))

for i in range(print_range):
    print(f'element {i} of combinations: {combination_list[i]}')


# need to find "THE" 3 wires which can be disconnected to separate the components into 2 separate groups
def solve():
    answer = 1
    return answer
'''
I could develop a function which will return 1 for the original data
...but will return 2 when the 3 wires in the example are 'cut'.
This could work by randomly testing two components to see if they are connected or not.
There should be a 1 in 2 chance that they are connected, so testing 20 point pairs should give a 1 in 1048576 chance of false negative.

'''

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