#!/usr/bin/env python3
# https://adventofcode.com/2022/day/1
print("hola bethel")
calorie_string = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""
# elves=[]
# food = []
# for line in calorie_string.splitlines():
#     if line == "":
#         # make elf
#         elves.append(food)
#         food=[]
#     else:
#         food.append(int(line))

# elves.append(food)
# print (elves)

# maximum = 0
# for elf in elves:
#     if sum(elf)>maximum:
#         maximum = sum(elf)
# print(maximum)

calories = 0
max_calories = 0
for line in calorie_string.splitlines():
    if line != "":
        calories = calories + int(line)

    else:
        if max_calories < calories:
            max_calories = calories
        calories = 0
print(max_calories)
