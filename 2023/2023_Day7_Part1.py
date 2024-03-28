#!/usr/bin/env python3
#https://adventofcode.com/2023/day/7

with open("2023/2023_Day7_input.txt") as file_object: # test_input should give a total_winnings of 6440
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

for index,line in enumerate(file_content):
    hand = line.split()[0]
    bid = int(line.split()[1])
    print("line index: ", index,", hand: ",hand,", bid: ",bid)
    cards = {}
    for card in hand:
        if card not in cards:
            cards[card] = 1
        else:
            cards[card] += 1
    print(cards)
    values_list = list(cards.values())
    max_value = max(values_list)
    print("max value: ",max_value)
    #cards["line index"] = index
    cards["bid"] = bid
    if max_value is 5:
        five_of_a_kind.append(cards)
    elif max_value is 4:
        four_of_a_kind.append(cards)
    elif max_value is 3:
        if 2 in cards.values():
            full_house.append(cards)
        else:
            three_of_a_kind.append(cards)
    elif max_value is 2:
        if values_list.count(2) is 2:
            two_pairs.append(cards)
        else:
            one_pair.append(cards)
    else:
        high_card.append(cards)
#print('5 of a kind: ',five_of_a_kind,'\n4 of a kind: ',four_of_a_kind,'\nfull house: ',full_house,'\n3 of a kind: ',three_of_a_kind,'\n2 pair: ',two_pairs,'\n1 pair: ',one_pair,'\nhigh card: ',high_card)

for card in card_ranking:
    for hand in five_of_a_kind:
        if card in hand.keys():
            print('card ',card,' found')
            five_of_a_kind.remove(hand)
            five_of_a_kind.append(hand)
            break
print(five_of_a_kind)

total_winnings = 0
all_hands = five_of_a_kind
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