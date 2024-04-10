#!/usr/bin/env python3
#https://adventofcode.com/2023/day/7

with open("2023/2023_Day7_input.txt") as file_object: # test_input should give a total_winnings of 6440: done
    file_content = file_object.readlines()

# a rank of 1 means the weakest hand

card_ranking = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
reverse_card_ranking = card_ranking[::-1]
secondary_ranking = ['J','2','3','4','5','6','7','8','9','T','Q','K','A']
full_input_list = []
five_of_a_kind = []
four_of_a_kind = []
full_house = []
three_of_a_kind = []
two_pairs = []
one_pair = []
high_card = []

def secondary_list_sorting(input_list):
    output_list = input_list
    for i in [4,3,2,1,0]:
        temporary_output = []
        for card in secondary_ranking:
            for line in output_list:
                if line [0][i] == card:
                    temporary_output.append(line)
        output_list = temporary_output
    return output_list

for j,line in enumerate(file_content):
    hand = line.split()[0]
    bid = int(line.split()[1])
    #print("line index: ", index,", hand: ",hand,", bid: ",bid)
    full_input_list.append([hand,bid])
    
secondary_ordered_list = secondary_list_sorting(full_input_list)

for line in secondary_ordered_list:
    hand,bid = line[0],line[1]
    cards = {}
    for card in hand:
        if card not in cards:
            cards[card] = 1
        else:
            cards[card] += 1
    #print(cards)
    values_list = list(cards.values())
    max_value = max(values_list)
    if 'J' in cards:
        number_of_jacks = cards['J']
        print(f'\n New hand found with Jack(s)! Hand: {hand} Jack(s) found: {number_of_jacks}')
        for card,value in cards.items():
            if card == 'J':
                continue
            print('card',card,'value',value)
            if max_value == 1:
                cards[card] = value + number_of_jacks
                print(f'highest unique card: {card} card quantities updated: ', cards)
                break
            if value > 1:
                print('highest card: ',card)
                cards[card] = value + number_of_jacks
                print('card quantities updated for multi-card: ', cards)
                break
    values_list = list(cards.values())
    max_value = max(values_list)
    print(f'max value: {max_value}')
    if max_value == 5:
        five_of_a_kind.append([hand,bid])
    elif max_value == 4:
        four_of_a_kind.append([hand,bid])
    elif max_value == 3:
        if 2 in values_list:
            full_house.append([hand, bid])
        else:
            three_of_a_kind.append([hand,bid])
    elif max_value == 2:
        if values_list.count(2) == 2:
            #print('Two pairs found!, Cards are: ',cards
            two_pairs.append([hand,bid])
        else:
            one_pair.append([hand,bid])
    else:
        high_card.append([hand,bid])
#print('5 of a kind: ',five_of_a_kind,'\n4 of a kind: ',four_of_a_kind,'\nfull house: ',full_house,'\n3 of a kind: ',three_of_a_kind,'\n2 pair: ',two_pairs,'\n1 pair: ',one_pair,'\nhigh card: ',high_card)


total_winnings = 0
all_hands = high_card + one_pair + two_pairs + three_of_a_kind + full_house + four_of_a_kind + five_of_a_kind
for i, hand in enumerate(all_hands):
    rank = i + 1
    bid = hand[1]
    #print('rank: ',rank,' cards: ',hand[0],' bid: ',bid)
    hand_winnings = rank * hand[1]
    total_winnings += hand_winnings

print('number of lines processed: ',rank)
print(f"total_winnings: {total_winnings}")

'''
The lowest ranked hands will be J2345, J2346, J2347...
The highest ranks will be AAAAA, AAAAJ, AAAJJ, ...      ..., QQQQJ, QQQJJ, QQJJJ, QJJJJ, TTTTT, ...

251976688: answer too low
252375781: answer too high

This method is not always choosing the correct card to up-value with jacks.
It is actually giving the ['J3TT3', 540] a higher rank than ['J22KK', 519].
In other words it is basing it off the 3 being higher than the 2.
It should actually be looking at the K being higher than the T.
'''