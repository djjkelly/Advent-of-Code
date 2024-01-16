#!/usr/bin/env python3
# https://adventofcode.com/2023/day/2

import re
colour_limits = {'green':13,'blue':14,'red':12}

total = 0 # the "total" variable counts the sum of the game numbers which is able to
try:
    with open("2023/2023_Day2_input.txt") as file_object:
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
    max_green = 0
    green = 0
    for round_count,round in enumerate(rounds,start=1):
        try:
            green_position = re.search("green",round).start()
            green = round[green_position-3] + round[green_position-2]
        except AttributeError:
            print("Round " + str(round_count) + " has no green")
            continue
        print ("Round " + str(round_count) + ". Number of greens found: " + green)
        if int(green) > max_green:
            max_green = int(green)
    print("Game " + str(game_number) + " has a maximum number of " + str(max_green) +" greens.")
    green_possible = colour_limits['green']>=max_green
    if (green_possible):
        print("Based on green only, this could be possible")
