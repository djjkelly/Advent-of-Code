with open("2021/2021_Day2_input.txt") as file_object:
    file_content = file_object.readlines()

'''
Forward increases horizontal position * X AND increases depth by aim * X
Down increases aim by X
Up decreases aim by X
'''
aim = 0
horizontal_position = 0
depth = 0

for line in file_content:
    if "forward" in line:
        forward_number = int(line.split()[1])
        horizontal_position += forward_number
        depth += aim * forward_number

    if "down" in line:
        down_number = int(line.split()[1])
        aim += down_number

    if "up" in line:
        up_number = int(line.split()[1])
        aim -= up_number

answer = horizontal_position * depth
print(answer)