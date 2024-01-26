#!/usr/bin/env python3
#https://adventofcode.com/2023/day/5

try:
    with open("2023/2023_Day5_input.txt") as file_object:
        file_content = file_object.readlines()
    blank_lines = [0]*len(file_content)
    print(blank_lines)
    for line_number,line in file_content:
        if line == '\n':
            pass
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"An error was encountered: {e}")
