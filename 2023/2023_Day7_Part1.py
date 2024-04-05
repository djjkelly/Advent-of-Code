#!/usr/bin/env python3
#https://adventofcode.com/2023/day/7

with open("2023/2023_Day7_testinput.txt") as file_object: # test_input should give a total_winnings of 6440
    file_content = file_object.readlines()

# a rank of 1 means the weakest hand

card_ranking = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
five_of_a_kind = []
four_of_a_kind = []
full_house = []
three_of_a_kind = []
two_pairs = []
one_pair = []
high_card = []

def sort_list(input_list,input_int):
    sorted_list =[]
    for card in card_ranking:
        for hand in input_list:
            if card in hand.keys():
                if hand[card] == input_int:
                    sorted_list.append(hand)
    return sorted_list

for index,line in enumerate(file_content):
    hand = line.split()[0]
    bid = int(line.split()[1])
    #print("line index: ", index,", hand: ",hand,", bid: ",bid)
    cards = {}
    for card in hand:
        if card not in cards:
            cards[card] = 1
        else:
            cards[card] += 1
    #print(cards)
    values_list = list(cards.values())
    max_value = max(values_list)
    #print("max value: ",max_value)
    #cards["line index"] = index
    cards["bid"] = bid
    if max_value == 5:
        five_of_a_kind.append(cards)
    elif max_value == 4:
        four_of_a_kind.append(cards)
    elif max_value == 3:
        if 2 in cards.values():
            full_house.append(cards)
        else:
            three_of_a_kind.append(cards)
    elif max_value == 2:
        if values_list.count(2) == 2:
            two_pairs.append(cards)
        else:
            one_pair.append(cards)
    else:
        high_card.append(cards)
#print('5 of a kind: ',five_of_a_kind,'\n4 of a kind: ',four_of_a_kind,'\nfull house: ',full_house,'\n3 of a kind: ',three_of_a_kind,'\n2 pair: ',two_pairs,'\n1 pair: ',one_pair,'\nhigh card: ',high_card)

five_of_a_kind = sort_list(five_of_a_kind,5)
#print(five_of_a_kind)
four_of_a_kind = sort_list(four_of_a_kind,1)
four_of_a_kind = sort_list(four_of_a_kind,4)
#print(four_of_a_kind)
full_house = sort_list(full_house,2)
full_house = sort_list(full_house,3)
#print(full_house)

# This method is not suitable for sorting three of a kind, two pairs, pair, or high card.

total_winnings = 0
all_hands = full_house+four_of_a_kind+five_of_a_kind
for index,hand in enumerate(all_hands):
    rank = index +1
    hand_winnings = rank * hand['bid']
    total_winnings += hand_winnings
print(f"total_winnings: {total_winnings}")
'''
The lowest ranked hands will be 23456, 23457, 23458
The highest ranks will be AAAAA, KKKKK, QQQQQ...

I think my program needs to sort them into categories first, and then sort the categories.
'''