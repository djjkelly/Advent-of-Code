#!/usr/bin/env python3
#https://adventofcode.com/2023/day/17

folder = '2023/'
filename = '2023_Day17_input'
extension = '.txt'
full_path = folder + filename + extension

from testmodule import test_function

with open(full_path,'r') as file_object:
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
    heapq.heappush(queue, (0, 0, 0, 0, 0, 1))
#                         mhl v  h dv  dh st
    while queue:
        current_estimate, v, h, dv, dh, steps  = heapq.heappop(queue)
        if (v, h) == (vertical_length-1, horizontal_length-1) and 4 <= steps < 10:
            return current_estimate
        # Avoid revisiting unless current_loss is better
        state = (v, h, dv, dh, steps)
        if state in minimum_heat_loss_estimates and minimum_heat_loss_estimates[state] <= current_estimate:
            continue
        minimum_heat_loss_estimates[state] = current_estimate
        if steps < 10 and (dv,dh) != (0,0): # straight line case
            nv, nh = v + dv, h + dh
            if 0 <= nv < vertical_length and 0 <= nh < horizontal_length:
                new_estimate = current_estimate + input_list[nv][nh]
                heapq.heappush(queue, (new_estimate, nv, nh, dv, dh, steps + 1)) # using old direction vectors

        if steps >= 4 or (dv,dh) == (0,0): # changing direction case - starting at 0 is the same process as changing direction!
            for (ddv,ddh) in directions:
                if (ddv,ddh) == (-dv,-dh):
                    continue
                # Continue moving in the same direction if direction is permitted
                elif (ddv,ddh) != (dv,dh):
                    nv, nh = v + ddv, h + ddh
                    if 0 <= nv < vertical_length and 0 <= nh < horizontal_length:
                        new_estimate = current_estimate + input_list[nv][nh]
                        heapq.heappush(queue, (new_estimate, nv, nh, ddv, ddh, 1))
result = min_heat_loss(input_list)
print(f"\nMinimum heat loss: {result}")

test_dictionary = {
    '2023_Day17_input':{'attempts':(888,946),'low':946,'high':None,'answer':993},
    '2023_Day17_test1_input':{'answer':94},
    '2023_Day17_test2_input':{'answer':71}
}
test_function(test_dictionary,filename,result)
'''
Correct answer of 94 heat loss has been achieved for test1_input.
888 - answer too low.
946 - answer too low.

Correct answer obtained - 993
'''