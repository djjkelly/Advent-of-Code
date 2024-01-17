#!/usr/bin/env python3
# https://adventofcode.com/2023/day/2

import re

total = 0 # the "total" variable counts the sum of the game numbers which is able to
try:
    with open("2023/2023_Day2_input.txt") as file_object:
        file_content = file_object.readlines()
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"An error was encountered: {e}")

colours = {'green','blue','red'}

for game_number,line in enumerate(file_content,start=1):
    trimmed_line = line.strip().split(":")[1]
    # DK: I'm referring to the 3 "sets" of the game as each time the elf grabs a fistful of cubes
    sets = trimmed_line.split(";")
    print("Game "+ str(game_number) + " consisting of " + str(len(sets)) + " rounds...")
    game_power = 1
    for colour in colours:
        max_of_colour = 0
        number_of_cubes = 0 # of the specified colour
        for set_count,set in enumerate(sets,start=1):
            try:
                colour_position = re.search(colour,set).start()
                number_of_cubes = set[colour_position-3] + set[colour_position-2]
            except AttributeError:
                print("Set " + str(set_count) + " has no " + colour)
                continue
            print ("Set " + str(set_count) + ". Number of " + colour + "s found: " + number_of_cubes)
            if int(number_of_cubes) > max_of_colour:
                max_of_colour = int(number_of_cubes)
        print("Game " + str(game_number) + " has a maximum number of " + str(max_of_colour) + " " + colour + ".")
        game_power *= max_of_colour
    total += game_power
    print("Game power for game " + str(game_number) + " is " + str(game_power))
print(total)
