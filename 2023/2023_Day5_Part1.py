#!/usr/bin/env python3
#https://adventofcode.com/2023/day/5

import re
try:
    with open("2023/2023_Day5_input.txt") as file_object:
        file_content = file_object.readlines()

    data_dict = {}
    current_header = None
    current_lines = []

    def translate(current_number,key):
        #print(data_dict[key])
        for element in data_dict[key]:
            destination_start = element["Destination start point"]
            source_start = element["Source start point"]
            range_length = element["Range length"]
            destination_end = destination_start + range_length
            source_end = source_start + range_length
            print(f'Source range: {source_start} - {source_end}. Destination range: {destination_start} - {destination_end}')

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
    seeds = data_dict['seeds'][0].split()
    for seed_number in seeds:
        #print("This is seed number: ",seed_number)
        soil_number = translate(seed_number,"seed-to-soil map")
        #soil_number = 1
        fertiliser_number = 2
        water_number = 3
        light_number = 4
        temperature_number = 5
        humidity_number = 6
        location_number = 7

except FileNotFoundError:
    print("File not found")
    import os
    current_directory = os.getcwd()
    ls = os.listdir()
    print("Current working directory: ", current_directory, "\nCWD contains the following files or folders: ", ls)
except Exception as e:
    print(f"An error was encountered: {e}")
