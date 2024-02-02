with open("2021/2021_Day1_input.txt") as file_object:
    file_content = file_object.readlines()
list_of_integers = []
count = 0
for line in file_content:
    list_of_integers.append(int(line.strip()))

sample_size = 3

previous_value = sum(list_of_integers[0:sample_size])

for i in range(len(list_of_integers)):
    slice = list_of_integers[i:i+sample_size]
    line_sum = sum(slice)
    
    print(f"Slice: {slice}\nLine sum: {line_sum}")
    if line_sum > previous_value:
        count += 1
    previous_value = line_sum

print(count)
