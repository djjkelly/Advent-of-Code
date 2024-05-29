#!/usr/bin/env python3
#https://adventofcode.com/2023/day/17

filename = "2023/2023_Day17_test1_input.txt"

from testmodule import test_function

with open(filename,'r') as file_object:
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
                if steps < 4:
                    if 0 <= nv < vertical_length and 0 <= nh < horizontal_length:
                        new_estimate = current_estimate + input_list[nv][nh]
                        heapq.heappush(queue, (new_estimate, nv, nh, ddv, ddh, steps + 3))
                        print(f'steps = {steps}. steps < 4, new steps: {steps + 3}')
                        continue
                if 4 <= steps < 10:
                    if 0 <= nv < vertical_length and 0 <= nh < horizontal_length:
                        new_estimate = current_estimate + input_list[nv][nh]
                        heapq.heappush(queue, (new_estimate, nv, nh, ddv, ddh, steps + 1))
                        print(f'steps = {steps}. steps in eligible range - both continue and straight. new steps: {steps + 1}')
            # Try different directions:
            else:
                if 4 <= steps < 10:
                    if 0 <= nv < vertical_length and 0 <= nh < horizontal_length:
                        new_estimate = current_estimate + input_list[nv][nh]
                        heapq.heappush(queue, (new_estimate, nv, nh, ddv, ddh, 1))
                        print(f'steps = {steps}. turning to alternate directions! new steps = {1}')
result = min_heat_loss(input_list)
print(f"\nMinimum heat loss: {result}")

test_dictionary = {
    '2023/2023_Day17_input.txt':{'attempts':(888,946),'low':946,'high':None,'answer':None},
    '2023/2023_Day17_test1_input.txt':{'answer':94},
    '2023/2023_Day17_test2_input.txt':{'answer':71}
}
test_function(test_dictionary,filename,result)
'''
Correct answer of 94 heat loss has been achieved for test1_input.
888 - answer too low.
946 - answer too low.
'''