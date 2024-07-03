#!/usr/bin/env python3
# https://adventofcode.com/2023/day/2

import re

folder = '2023/'
filename = '2023_Day2_input'
extension = '.txt'
full_path = folder + filename + extension

colour_limits = {'green':13,'blue':14,'red':12}
colour_possible = {'green':True,'blue':True,'Red':True}

total = 0 # the "total" variable counts the sum of the game numbers which is able to
try:
    with open(full_path) as file_object:
        file_content = file_object.readlines()
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"An error was encountered: {e}")

for game_number,line in enumerate(file_content,start=1):
    trimmed_line = line.strip().split(":")[1]
    # DK: I'm referring to the 3 "rounds" of the game as each time the elf grabs a fistful of cubes
    rounds = trimmed_line.split(";")
    print("Game "+ str(game_number) +" consisting of " + str(len(rounds)) + " rounds...")
    for colour,limit in colour_limits.items():
        max_of_colour = 0
        number_of_cubes = 0 # of the specified colour
        for round_count,round in enumerate(rounds,start=1):
            try:
                colour_position = re.search(colour,round).start()
                number_of_cubes = round[colour_position-3] + round[colour_position-2]
            except AttributeError:
                print("Round " + str(round_count) + " has no " + colour)
                continue
            print ("Round " + str(round_count) + ". Number of " + colour + "s found: " + number_of_cubes)
            if int(number_of_cubes) > max_of_colour:
                max_of_colour = int(number_of_cubes)
        print("Game " + str(game_number) + " has a maximum number of " + str(max_of_colour) + " " + colour + ".")
        colour_possible[colour] = max_of_colour <= colour_limits[colour]
        if (colour_possible):
            print("Based on " + colour + " only, this could be possible")
        else:
            print("Not possible. Number of cubes exceeds limit for " + colour)
    all_colours_true = all(colour for colour in colour_possible.values())
    if all_colours_true:
        total += game_number
        print("This is true, game number " + str(game_number) + " added to total.")
    else:
        print("Game " + str(game_number) + " not possible with available cubes")
print(total)

'''
My answer was 2085
'''
test_dictionary = {
    '2023_Day2_input':
    {'answer':2085},
}

from testmodule import test_function
test_function(test_dictionary,filename,total)