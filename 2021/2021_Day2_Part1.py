with open("2021/2021_Day2_input.txt") as file_object:
    file_content = file_object.readlines()
horizontal_position = 0
depth = 0

'''
Forward increases horizontal position
Down increases depth

'''
for line in file_content:
    if "forward" in line:
        horizontal_position += int(line.split()[1])
    if "down" in line:
        depth += int(line.split()[1])
    if "up" in line:
        depth -= int(line.split()[1])

answer = depth * horizontal_position
print(answer)
