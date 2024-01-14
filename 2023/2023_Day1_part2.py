# https://adventofcode.com/2023/day/1
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
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    }
with open("2023/2023_Day1_input.txt") as file:
    total = 0
    for line in file:
        result = {"first_value" : None, "last_value" : None}
        for key in num_dict.keys():
            if key not in line:
                continue
            if result["first_valuasdfe"] is None:
                result["first_value"] = key
            else:
                if line.find(key) < line.find(result["first_value"]):
                    result["first_value"] = key

            if result["last_value"] is None:
                result["last_value"] = key
            else:
                if line[::-1].find(key[::-1]) < line[::-1].find(result["last_value"][::-1]):
                    result["last_value"] = key
        line_total = int(num_dict.get(result["first_value"])+num_dict.get(result["last_value"]))
        print(f"{line.strip()} => {line_total}")
        total += int(num_dict.get(result["first_value"])+num_dict.get(result["last_value"]))
print (total)