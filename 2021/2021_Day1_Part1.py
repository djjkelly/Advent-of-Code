with open("2021/2021_Day1_input.txt") as file_object:
    file_content = file_object.readlines()
list_of_integers = []
total = 0
for line in file_content:
    list_of_integers.append(int(line.strip()))
previous_value = list_of_integers[0]
for element in list_of_integers:
    if element > previous_value:
        total += 1
    previous_value = element

print(total)
