#!/usr/bin/env python3
#https://adventofcode.com/2023/day/6

with open("2023/2023_Day6_input.txt") as file_object:
    file_content = file_object.readlines()

time_input = [int(x) for x in file_content[0].split(': ')[1].split()]
distance_input = [int(x) for x in file_content[1].split(': ')[1].split()]
print("time input: ",time_input,"distance input: ",distance_input)

#test_time_input,test_distance_input = [7,15,30],[9,40,200]
#time_input,distance_input = test_time_input,test_distance_input
#print("test time input: ",time_input,"test distance input: ",distance_input) # test should give rise to a product of 288 as per example on website

ways_to_win_list = []

for race in range(len(time_input)):
    ways_to_win = 0
    race_time,distance_record = time_input[race],distance_input[race]
    print("Race ",race, ": race time: ",race_time,", distance record: ",distance_record)
    for speed in range(race_time+1):
        distance = speed * (race_time - speed)
        print("speed: ",speed,"distance: ",distance)
        if distance > distance_record:
            ways_to_win += 1
    print("ways to win :", ways_to_win)
    ways_to_win_list.append(ways_to_win)
product = 1
for factor in ways_to_win_list:
    product *= factor
print(product)
