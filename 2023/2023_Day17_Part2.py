#!/usr/bin/env python3
#https://adventofcode.com/2023/day/17

with open("2023/2023_Day17_input.txt",'r') as file_object:
    file_content = file_object.readlines()
input_list = []
for line in file_content:
    line = line.strip()
    input_list.append([int(char) for char in line])
horizontal_length = len(line)
vertical_length = len(input_list)
directions = [(1,0), (0,1), (-1,0), (0,-1)]

import heapq

def min_heat_loss(input_list):
    vertical_length, horizontal_length = len(input_list), len(input_list[0])
    
    queue = []
    minimum_heat_loss_estimates = {}
    heapq.heappush(queue, (0, 0, 0, 0, 1, 1))  # Start by moving right
    heapq.heappush(queue, (0, 0, 0, 1, 0, 1))   # Start by moving down
#                         mhl v  h dv  dh st
    while queue:
        current_estimate, v, h, dv, dh, steps  = heapq.heappop(queue)
        if (v, h) == (vertical_length-1, horizontal_length-1):
            return current_estimate
        # Avoid revisiting unless current_loss is better
        state = (v, h, dv, dh, steps)
        if state in minimum_heat_loss_estimates and minimum_heat_loss_estimates[state] <= current_estimate:
            continue
        minimum_heat_loss_estimates[state] = current_estimate
        for (ddv,ddh) in directions:
            if (ddv,ddh) == (-dv,-dh):
                continue
            # Continue moving in the same direction if direction is permitted
            nv, nh = v + ddv, h + ddh
            if (ddv,ddh) == (dv,dh):
                if steps < 10:
                    if 0 <= nv < vertical_length and 0 <= nh < horizontal_length:
                        new_estimate = current_estimate + input_list[nv][nh]
                        heapq.heappush(queue, (new_estimate, nv, nh, ddv, ddh, steps + 1))
            # Try different directions:
            elif 0 <= nv < vertical_length and 0 <= nh < horizontal_length:
                new_estimate = current_estimate + input_list[nv][nh]
                heapq.heappush(queue, (new_estimate, nv, nh, ddv, ddh, 1))
result = min_heat_loss(input_list)
print(f"Minimum heat loss: {result}")

if result <= 946:
    print('wrong answer - too low!')
'''
888 - answer too low.
946 - answer too low.
'''