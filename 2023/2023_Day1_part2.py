num_dict = {
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9',
    }
with open("2023/2023_Day1_input.txt") as file:
    total = 0
    for line in file:
        numerical_line = line
        for key,value in num_dict.items():
            numerical_line = numerical_line.replace(key,value)
        print(line.strip())
        print(numerical_line.strip())
        for char in numerical_line:
            if char.isnumeric():
                print(char)
                first_digit = char
                break
        reversed_line = numerical_line[::-1]
        print(reversed_line.strip())
        for char in reversed_line:
            if char.isnumeric():
                print(char)
                last_digit = char
                break
        total += int(first_digit+last_digit)
        print(total)
print (total)