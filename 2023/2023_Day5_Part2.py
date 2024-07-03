#!/usr/bin/env python3
#https://adventofcode.com/2023/day/5

folder = '2023/'
filename = '2023_Day5_input'
extension = '.txt'
full_path = folder + filename + extension

import re
try:
    with open(full_path) as file_object:
        file_content = file_object.readlines()

    data_dict = {}
    current_header = None
    current_lines = []
    minimum_location_number = float('inf')

    def translate(current_number,key):
        #print(data_dict[key])
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
                #print(f'The number is not translated')
                continue
        if not result:
            #print(f"Returning current number {current_number}")
            return(current_number)

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
    #print(data_dict)
    seeds_list = data_dict['seeds'][0].split()
    print(seeds_list)
    length = int(len(seeds_list)/2)
    seeds = []
    for number in range(length):
        range_start = int(seeds_list[number*2])
        range_length = int(seeds_list[number*2+1])
        #print(f'The range starts at {range_start} and has a length of {range_length}')
        seeds_sublist = list(range(range_start,range_start+range_length))
        seeds.extend(seeds_sublist)
    print(len(seeds)) # this prints 1934995782 which is correct
    seeds = list(set(seeds))
    print(len(seeds))

    for seed_number in seeds:
        soil_number = translate(seed_number,"seed-to-soil map")
        fertiliser_number = translate(soil_number,"soil-to-fertilizer map")
        water_number = translate(fertiliser_number,"fertilizer-to-water map")
        light_number = translate(water_number,"water-to-light map")
        temperature_number = translate(light_number,"light-to-temperature map")
        humidity_number = translate(temperature_number,"temperature-to-humidity map")
        location_number = translate(humidity_number,"humidity-to-location map")
        if location_number < minimum_location_number:
            minimum_location_number = location_number
    print(f'The minimum location number is {minimum_location_number}')

except FileNotFoundError:
    print("File not found")
    import os
    current_directory = os.getcwd()
    ls = os.listdir()
    print("Current working directory: ", current_directory, "\nCWD contains the following files or folders: ", ls)
except Exception as e:
    print(f"An error was encountered: {e}")

test_dictionary = {
    '2023_Day5_input':
    {'answer':37384986},
}

from testmodule import test_function
test_function(test_dictionary,filename,minimum_location_number)