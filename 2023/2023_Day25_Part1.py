#!/usr/bin/env python3
#https://adventofcode.com/2023/day/25

from random import randint, choice
import networkx as nx
import matplotlib.pyplot as plt
import community
from statistics import mode

folder = '2023/'
filename = '2023_Day25_input'
extension = '.txt'
full_path = folder + filename + extension
with open(full_path,'r') as file_object:
    file_content = file_object.readlines()

def consistent_split(string):
    if len(string.split()) == 1:
        return [string.strip()]
    else:
        return string.split()

def prepare_data(file_content):
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
    #for wire in wires_list:
        #print(wire)
    return connections, input_dict, components_list, wires_list
connections ,input_dict , components_list , wires_list = prepare_data(file_content)

def process_graph(components_list,wires_list):
    Graph = nx.Graph()
    components_list = [sublist[0] for sublist in components_list]
    Graph.add_nodes_from(components_list)
    Graph.add_edges_from(wires_list)
    partition = community.best_partition(Graph)
    print(partition)
    inter_community_edges = []

    community_numbers_counts = {}
    for node,community_no in partition.items():
        if community_no not in community_numbers_counts:
            community_numbers_counts[community_no] = 1
        else:
            community_numbers_counts[community_no] += 1
    print(community_numbers_counts)
    for (u, v) in Graph.edges():
        if partition[u] != partition[v]:
            inter_community_edges.append((u, v))
        

    print("Edges to remove to separate the communities:", inter_community_edges)


    new_partition = community.best_partition(Graph)
    print(new_partition)
    target_community = mode(new_partition.values())
    count1,count2 = 0,0
    for node, community_no in new_partition.items():
        if community_no == target_community:
            count1+=1
        elif isinstance(node,str):
            count2+=1
    print('count1:',count1,'count2:',count2)
    total = count1 * count2
    return total
total = process_graph(components_list,wires_list)
print('total:',total)
test_dictionary = {
    '2023_Day25_input':
    {'attempts':(356717,),
    'low':356717,'high':None,'answer':None},
    '2023_Day25_testinput':
    {'answer':54},
}

from testmodule import test_function
test_function(test_dictionary,filename,total)
'''
Correct answer obtained for testinput.
356717 is not the right answer
This gives a different answer each time.

'''