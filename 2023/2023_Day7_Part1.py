#!/usr/bin/env python3
#https://adventofcode.com/2023/day/7

with open("2023/2023_Day7_testinput.txt") as file_object: # test_input should give a total_winnings of 6440
    file_content = file_object.readlines()

# a rank of 1 means the weakest hand

card_ranking = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
for index,line in enumerate(file_content):
    hand = line.split()[0]
    bid = int(line.split()[1])
    print("line index: ", index," hand: ",hand," bid: ",bid)

#hand_winnings = rank * bid

primary_order = [] # based on type
secondary_order = [] # based on card value

total_winnings = 0
print(f"total_winnings: {total_winnings}")

# full_house
# five_of_a_kind
# four_of_a_kind
# three_of_a_kind
# two_pair
# pair

'''
The lowest ranked hands will be 23456, 23457, 23458
The highest ranks will be AAAAA, KKKKK, QQQQQ...

I think my program needs to sort them into categories first, and then sort the categories.
'''