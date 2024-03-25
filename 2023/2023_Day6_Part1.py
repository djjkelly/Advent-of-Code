#!/usr/bin/env python3
#https://adventofcode.com/2023/day/6

with open("2023/2023_Day6_input.txt") as file_object:
    file_content = file_object.readlines()

time_input = [int(x) for x in file_content[0].split(': ')[1].split()]
distance_input = [int(x) for x in file_content[1].split(': ')[1].split()]

