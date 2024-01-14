#!/usr/bin/env python3
import re
#colours = ('green','blue','red')

# digits is a modifiable parameter determining how many characters should be scanned in the string
# this is the maximum number of digits required to represent the cubes expected in the game.
# in this instance of the game there are no numbers above 99, so 2 digits is ok.
digits = 2

try:
    with open("2023/2023_Day2_input.txt") as file_object:
        file_content = file_object.readlines()
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"An error was encountered: {e}")
for line in file_content:
    split_line = line.strip().split(";")
    max_green = 0
    max_red = 0
    max_blue = 0
    for grab in split_line:
        try:
        green_position = re.search("green",grab).start()
except Exception as error:
        green = ""
        green = grab[green_position-2] + grab[green_position-1]
        green = int(green.strip())
        if green > max_green:
            max_green = green
    print(line)
    print(max_green)
