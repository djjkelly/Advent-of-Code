#!/usr/bin/env python3
#https://adventofcode.com/2023/day/5

folder = '2023/'
filename = '2023_Day5_input'
extension = '.txt'
full_path = folder + filename + extension

import re
with open(full_path) as file_object:
    file_content = file_object.readlines()

def parse_file_content(file_content):
    data_dict = {}
    current_header = None
    current_lines = []
    for line_number,line in enumerate(file_content):
        line = line.strip()
        if line:
            if ":" in line:
                #Header found!
                if current_header is not None:
                    data_dict[current_header] = current_lines
                    current_lines = []
                current_header = line.split(':')[0].strip()
                if line.split(':')[1]:
                    current_lines.append(line.split(':')[1])
            else:
                three_numbers = [int(num) for num in line.split()]
                current_lines.append({"Destination start point":three_numbers[0],"Source start point":three_numbers[1],"Range length":three_numbers[2]})
    if current_header is not None and current_lines:
        data_dict[current_header] = current_lines
    seeds_list = data_dict['seeds'][0].split()
    return seeds_list,data_dict

def convert_numbers_to_ranges(seeds_list): # express the seed numbers as ranges
    seeds_ranges = []
    for number in range(int(len(seeds_list)/2)):
        range_start = int(seeds_list[number*2])
        range_length = int(seeds_list[number*2+1])
        range_end = range_start + range_length - 1
        #print(f'The range starts at {range_start} and ends at {range_end}')
        seeds_ranges.append([range_start,range_end])
    return(seeds_ranges)
#print(f'convert_numbers_to_ranges {[50,13,69,12]}')

def sort_ranges(seeds_ranges): # sorting and removing duplicates from ranges (it turns out there are no duplicates anyway!)
    sorted_ranges = sorted(seeds_ranges,key=lambda x: x[0])
    merged = True
    while merged:
        merged = False
        i = 0
        while i < len(sorted_ranges)-1:
            current_range = sorted_ranges[i]
            next_range = sorted_ranges[i+1]
            #print("current range: ",current_range, " current range type:", type(current_range))
            if current_range[1] >= next_range[0]:
                merged_range = [current_range[0],max(current_range[1],next_range[1])]
                sorted_ranges[i] = merged_range
                del sorted_ranges[i+1]
                merged = True
            else:
                i += 1
    #print(f'Sorted ranges: {sorted_ranges}')
    return(sorted_ranges)

def translate(current_number,key): # THE ORDER IS WEIRD!...   DESTINATION > SOURCE > RANGE
    for element in data_dict[key]:
        result = None
        destination_start = int(element["Destination start point"])
        source_start = int(element["Source start point"])
        range_length = int(element["Range length"])-1
        source_end = int(source_start + range_length)
        #print(f'Source range: {source_start} - {source_end}.')
        if current_number >= source_start and current_number <= source_end:
            result = current_number - source_start + destination_start
            #print(f'The source range contains the current number! Returning {result}')
            return(result)
        else:
            continue
    if not result:
        return(current_number)
#print(f'translate test: {translate(50,"seed-to-soil map")}')

def split_range(input_range):
    start, end = input_range
    midpoint = (start + end)// 2
    return [[start, midpoint],[midpoint+1,end]]
#print(f'split_range test: {split_range([1500,4500])}')

def is_range_continuous(input_range,output_range):
    [input_start,input_end] = input_range
    [output_start, output_end] = output_range
    if output_end - output_start == input_end - input_start:
        range_continuous = True
    else:
        range_continuous = False
    if input_start == output_start and input_end != output_end:
        range_continuous = False
    if input_end == output_end and input_start != output_start:
        range_continuous = False
    return(range_continuous)
#print(f'is_range_continuous test: {is_range_continuous([100,210],[200,310])}') #should be True
#print(f'is_range_continuous test: {is_range_continuous([100,210],[200,311])}') #should be False

def translate_continuous_ranges(initial_input_range,key):
    continuous_ranges = [initial_input_range.copy()]
    translated_continuous_ranges = []
    index = 0
    while index < len(continuous_ranges):
        range_to_check = continuous_ranges[index]
        start, end = range_to_check
        # Translate the range
        translated_range = [translate(start, key), translate(end, key)]
        # Check if the range is continuous
        if is_range_continuous(range_to_check, translated_range):
            translated_continuous_ranges.append(translated_range)
            index += 1
            continue
        # If the range is not continuous, split it
        split_ranges = split_range(range_to_check)
        # Replace the current range with the split ranges
        continuous_ranges[index:index + 1] = split_ranges
    return translated_continuous_ranges
#print(f'test return value based on [50,70]: {make_all_ranges_continuous([50,70],"seed-to-soil map")}')

keys = ["seed-to-soil map","soil-to-fertilizer map","fertilizer-to-water map","water-to-light map","light-to-temperature map","temperature-to-humidity map","humidity-to-location map"]
seeds_list,data_dict = parse_file_content(file_content)
seeds_ranges = convert_numbers_to_ranges(seeds_list)
sorted_seeds_ranges = sort_ranges(seeds_ranges)
print(f'sorted_seeds_ranges {sorted_seeds_ranges}')

def find_minimum_location_number(sorted_seeds_ranges,keys):
    minimum_location_number = float('inf')
    next_ranges = sorted_seeds_ranges
    for key in keys:
        print("evaluating key: ",key)
        sorted_ranges = sort_ranges(next_ranges)
        translated_continuous_ranges = []
        for range in sorted_ranges:
            print('Starting new range: ',range)
            translated_continuous_ranges.extend(translate_continuous_ranges(range,key))
        print(translated_continuous_ranges)
        next_ranges = translated_continuous_ranges
    if key == "humidity-to-location map":
        location_ranges = translated_continuous_ranges
        print("Location ranges: ",location_ranges)
        for location_range in location_ranges:
            if min(location_range) < minimum_location_number:
                minimum_location_number = min(location_range)
        print(f'The minimum location number is {minimum_location_number}')
    return minimum_location_number
minimum_location_number = find_minimum_location_number(sorted_seeds_ranges,keys)

test_dictionary = {
    '2023_Day5_input':
    {'answer':37384986},
}

from testmodule import test_function
test_function(test_dictionary,filename,minimum_location_number)