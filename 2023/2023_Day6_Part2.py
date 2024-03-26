#!/usr/bin/env python3
#https://adventofcode.com/2023/day/6

with open("2023/2023_Day6_input.txt") as file_object:
    file_content = file_object.readlines()

time_input = ''.join(file_content[0].split(': ')[1].split())
distance_input = ''.join(file_content[1].split(': ')[1].split())
print("time input: ",time_input,"distance input: ",distance_input)

#test_time_input,test_distance_input = 71530,940200
#time_input,distance_input = test_time_input,test_distance_input
#print("test time input: ",time_input,"test distance input: ",distance_input) # test should give rise to a product of 71503 as per example on website

ways_to_win = 0
race_time,distance_record = int(time_input),int(distance_input)
#print("race time: ",race_time,", distance record: ",distance_record)
for speed in range(race_time+1):
    distance = speed * (race_time - speed)
    #print("speed: ",speed,"distance: ",distance)
    if distance > distance_record:
        ways_to_win += 1
print("ways to win :", ways_to_win) # correct answer found - 36872656. this is quite a slow method which takes about 15 seconds on my computer.
